import os, config
from dotenv import load_dotenv
from llama_index import StorageContext, load_index_from_storage
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY

# Load the data
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

# Set the query engine
query_engine = index.as_query_engine()
response = query_engine.query("What are some near-term risks to Nvidia?")

print(response)