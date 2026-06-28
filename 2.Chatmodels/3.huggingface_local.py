from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
llm = HuggingFacePipeline.from_model_id(
    model_id='zai-org/GLM-5.2',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
    )

)
model = ChatHuggingFace(llm=llm)
result = model.invoke("how many continents there are in the world")
print(result.content)