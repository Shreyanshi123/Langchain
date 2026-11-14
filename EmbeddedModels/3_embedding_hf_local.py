# the open source model for embedding is sentence-transformers/all-MiniLM-L6-v2
#  384 dimensional dense vector space and can be used like clustering or semantic search

from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Seoul is the capital of South Korea. Tokyo is the capital of Japan. Russia's capital is Moscow."

result = embeddings.embed_query(text)
print(result)

