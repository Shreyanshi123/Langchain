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


query = "tell me about the capital of south korea"

doc_embeddings = embeddings.embed_documents(capitals)
query_embedding = embeddings.embed_query(query)

# in case of cosine similarity whatever we are passing has to be a two d list 
scores = cosine_similarity([query_embedding], doc_embeddings)[0]
# it tells the similarity between the red vector query and the five black vectors capitals

index , score = sorted(list(enumerate(scores)), key = lambda x:x[1])[-1]
# sorting based on the second value

print (capitals[index])

print("similarity score: ", float(score))






