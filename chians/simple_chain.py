from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template="give a detail summary of 5 lines about {topic}",
    input_variables=["topic"]
)
model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.7)

parser = StrOutputParser()
chain = prompt | model | parser

result = chain.invoke({"topic": input("Enter a topic: ")})
print(result)