import datasets
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


knowledgebase = datasets.load_dataset("m-ric/huggingface_doc", split="train")

knowledgebase = knowledgebase.filter(lambda row:row["source"].startswith("huggingface/transformers"))

source_docs = [
    Document(page_content=doc["text"], metadata={"source":doc["source"].split("/")[1]})
    for doc in knowledgebase
]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    add_start_index=True,
    strip_whitespace=True,
    separators=["\n\n", "\n", ".", " ", ""]
)

docs_processed = text_splitter.split_documents(source_docs)

print(f"knowledgebase size: {len(docs_processed)} chunks")
