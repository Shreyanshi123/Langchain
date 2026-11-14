from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

embeddings = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions = 300)

capitals = [
    "Seoul is the capital of South Korea.",
    "Tokyo is the capital of Japan.",
    "Moscow is the capital of Russia.",
    "Edinburgh is the capital of Scotland."
]

