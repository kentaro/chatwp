import sys

import logging
logging.basicConfig(level=logging.WARNING)

from llama_index import GPTSimpleVectorIndex, LLMPredictor
from langchain import OpenAI

llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, max_tokens=1024))
index = GPTSimpleVectorIndex.load_from_disk("data/wordpress.json")

print("Question: ", end="", flush=True)

try:
  while question := next(sys.stdin).strip():
    output = index.query(question + "Be sure to include the URL of the source in your response.", llm_predictor=llm_predictor)
    print("Answer: ", end="")
    print(output)
    print("")
    print("Question: ", end="", flush=True)
except KeyboardInterrupt:
  pass
