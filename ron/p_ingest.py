import os

from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

loader = DirectoryLoader(
    "knowledge_base/",
    glob="**/*.md",
    loader_cls=TextLoader
)

documents = loader.load()

print(f"Loaded {len(documents)} documents successfully...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

print(f"Split into {len(chunks)} chunks...")

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pc.Index(
    os.getenv("PINECONE_INDEX_NAME")
)

records = []

for i, chunk in enumerate(chunks):
    records.append({
        "_id": f"chunk-{i}",
        "text": chunk.page_content,
        "source": chunk.metadata.get("source", "")
    })

index.upsert_records(
    namespace="portfolio",
    records=records
)

print("Documents uploaded to Pinecone!")