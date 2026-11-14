from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
import os


# os.environ["HF_HOME"] = 'D:/huggingface_cache' 
load_dotenv()


llm = HuggingFacePipeline.from_model_id(
    model_id="google/gemma-3-27b-it",
    task = "text-generation",
    pipeline_kwarys = dict(
        temperature = 0.5,
        max_new_tokens = 100,
    )
)

model = ChatHuggingFace(llm= llm)

response = model.invoke("What is the capital of Russia?")
print(response.content)

