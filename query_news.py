import os
from dotenv import load_dotenv
from llama_index import StorageContext, load_index_from_storage
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the data
storage_context = StorageContext.from_defaults(persist_dir="index_news.json")
index = load_index_from_storage(storage_context)

