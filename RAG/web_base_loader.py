from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
url='https://www.merriam-webster.com/dictionary/parse'
loader = WebBaseLoader(url)
docs = loader.load()

prompt = PromptTemplate(
    template="answer the following \n {question} from the given {text}",
    input_variables=["question","text"]
)
model = ChatGroq(model='openai/gpt-oss-20b')
parser = StrOutputParser()

chain = prompt |  model | parser
result = chain.invoke({"question":"what is parser", "text":docs[0].page_content})
print(result)