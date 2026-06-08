import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

loader = DirectoryLoader(
    'knowledge_base/',
    glob="**/*.md",
    loader_cls=TextLoader
)

documents = loader.load()
print(f'Loaded {len(documents)} documents successfully...')

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)
print(f'Split into {len(chunks)} chunks...')

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_TOKEN")
)

vector_store = FAISS.from_documents(chunks, embeddings)
vector_store.save_local("vector_store")
print("Vector store saved...")