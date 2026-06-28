from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

model = OpenAI("gpt-4")
result = model.invoke("whats the capital of usa")
print(result)
