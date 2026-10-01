from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model="openai/gpt-oss-20b",temperature=1.5)
chat_history = [
    SystemMessage(content='you are a ai assistant')
]

while True:
    user = input("You: ")
    chat_history.append(HumanMessage(content=user))
    if user == "exit":
        break
    result= model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("ai: ",result.content)
print(chat_history)
    