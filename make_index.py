import os

url = os.environ.get("WORDPRESS_URL")
username = os.environ.get("WORDPRESS_USERNAME")
password = os.environ.get("WORDPRESS_PASSWORD")

from llama_index import GPTSimpleVectorIndex, download_loader
from llama_index.langchain_helpers.chatgpt import ChatGPTLLMPredictor

WordpressReader = download_loader("WordpressReader")

loader = WordpressReader(url=url, username=username, password=password)
documents = loader.load_data()

index = GPTSimpleVectorIndex(documents, llm_predictor=ChatGPTLLMPredictor())
index.save_to_disk("data/wordpress.json")
