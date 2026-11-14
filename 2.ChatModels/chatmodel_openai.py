from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# thers a parameter called temperature whose value is between 0 and 2 
# creativity paramter
# smaller value means more deterministic and larger value means more creative

# we have another paramter called max_completion_tokens which is the maximum number of tokens that the model can generate in a single response.
model= ChatOpenAI(model="gpt-4o-mini", temperature=1.8, max_completion_tokens=10)

response =model.invoke("Tell me a joke about a cat and a dog.")

# print(response)
print(response.content)

# content='The capital of Japan is Tokyo.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 7, 'prompt_tokens': 13, 'total_tokens': 20, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0, 'text_tokens': None}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': None, 'cached_tokens': 0,'image_tokens': None, 'text_tokens': None}}, 'model_provider': 'openai', 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_15014e7912', 'id': 'chatcmpl-Ejp1o0ex6jFmbY7qZzRvEVjLa6DPS', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--01a1d5e0-769b-7368-835e-fb54d300b4cb-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 13, 'output_tokens': 7, 'total_tokens':20, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

