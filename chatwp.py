import sys

import logging
logging.basicConfig(level=logging.WARNING)

from llama_index import GPTSimpleVectorIndex, LLMPredictor
from llama_index.langchain_helpers.chatgpt import ChatGPTLLMPredictor
from langchain import OpenAI

prompt = """
Answer the question below based on the blog's content as if you were the author.

Question: {question}

Answer to the question in the same language as the question.
Be sure to include the URL of the source in your response as possible.
"""
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, max_tokens=1024))
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
