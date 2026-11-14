from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv  

load_dotenv()

llm = HuggingFaceEndpoint(
    model="google/gemma-3-27b-it",
    task="text-generation",
)

model = ChatHuggingFace(llm = llm)

response = model.invoke("What is the capital of Russia?")

print(response.content)


