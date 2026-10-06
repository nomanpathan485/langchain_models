from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")
parser = StrOutputParser()

prompt = PromptTemplate(
    template="write a summary for given poem - \n{text}",
    input_variables=["text"]
)
loader = TextLoader(r"C:\Users\Developer\Desktop\nom1\langchain_model\rag\cricket.txt", encoding="utf-8")
docs = loader.load()
chian = prompt | model | parser
result=chian.invoke({"text":docs[0].page_content})
print(result)