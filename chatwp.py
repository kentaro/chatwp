import sys
import fire
import logging

import os
if os.environ.get("OPENAI_API_KEY") == "":
  print("`OPENAI_API_KEY` is not set", file=sys.stderr)
  sys.exit(1)

url = os.environ.get("WORDPRESS_URL")
username = os.environ.get("WORDPRESS_USERNAME")
password = os.environ.get("WORDPRESS_PASSWORD")

from llama_index import GPTSimpleVectorIndex, download_loader
from llama_index.langchain_helpers.chatgpt import ChatGPTLLMPredictor

from llama_index import GPTSimpleVectorIndex, LLMPredictor
from langchain.llms import OpenAI

def run(make_index=False, verbose=False):
  if verbose:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.WARNING)

  if make_index:
    do_make_index()
  else:
    do_chat()

def do_make_index():
  WordpressReader = download_loader("WordpressReader")

  loader = WordpressReader(url=url, username=username, password=password)
  documents = loader.load_data()

  index = GPTSimpleVectorIndex(documents, llm_predictor=ChatGPTLLMPredictor())
  index.save_to_disk("data/wordpress.json")

def do_chat():
  prompt = """
Answer the question below based on the blog's content as if you were the author.

Question: {question}

Answer to the question in the same language as the question.
"""
  llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, max_tokens=1024))

  print("Loading index...")

  index = GPTSimpleVectorIndex.load_from_disk(
    "data/wordpress.json",
    llm_predictor=llm_predictor,
  )

  print("Question: ", end="", flush=True)
  try:
    while question := next(sys.stdin).strip():
      output = index.query(prompt.format(question=question))
      print("Answer: ", end="")
      print(output)
      print("")
      print("Question: ", end="", flush=True)
  except KeyboardInterrupt:
    pass

if __name__ == '__main__':
  fire.Fire(run)
