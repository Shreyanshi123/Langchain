from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# jyda dimension ka vector jyda context capture 

embeddings = OpenAIEmbeddings(model ='text-embedding-3-large', dimensions = 32)

# text-embedding-3- small 1536 and the 3072 for text-embedding-3-large

result = embeddings.embed_query("Seoul is the capital of South Korea.")
print(str(result))
