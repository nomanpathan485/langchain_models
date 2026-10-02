from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="give a detail research on the {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="give a summary of 5 lines about {text}",
    input_variables=["text"]
)
model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.7)
parser = StrOutputParser()
chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({"topic": input("Enter a topic: ")})
print(result)