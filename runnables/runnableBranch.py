from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableParallel, RunnableSequence, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='generate a detail report on {topic}',
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="summarize the following \n{text}",
    input_variables=["text"]
)

model = ChatGroq(model='openai/gpt-oss-20b')
parser = StrOutputParser()

report_generation_chain = RunnableSequence(prompt1, model, parser)
branch_chain = RunnableBranch(
    (lambda x : len(x.split())>500, RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

chain = RunnableSequence(report_generation_chain,branch_chain)
result = chain.invoke({"topic":input("enter topic: ")})
print(result)