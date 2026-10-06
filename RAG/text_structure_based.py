from langchain_text_splitters import RecursiveCharacterTextSplitter

text = "Soon, heavy rain began to fall. People hurried along the streets with umbrellas, while cars moved slowly through the wet roads. The sound of rain made the neighbourhood feel calm and peaceful."

splitter = RecursiveCharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=5
)
chunks = splitter.split_text(text)
print(chunks)