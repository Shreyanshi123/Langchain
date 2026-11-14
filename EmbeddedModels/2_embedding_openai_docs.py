# multiple query/ docs ka ek saath embedding karne ke liye
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# jyda dimension ka vector jyda context capture 

embeddings = OpenAIEmbeddings(model ='text-embedding-3-large', dimensions = 32)

# text-embedding-3- small 1536 and the 3072 for text-embedding-3-large


capitals = [
    "Seoul is the capital of South Korea.",
    "Tokyo is the capital of Japan.",
    "Russia's capital is Moscow."
]

result = embeddings.embed_documents(capitals)
print(str(result))



