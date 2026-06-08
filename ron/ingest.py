import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

loader = DirectoryLoader(
    'knowledge_base/',
    glob = "**/*.md",
    loader_cls=TextLoader
)

documents = loader.load()
print(f'Loader {len(documents)} documents successfully...')

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 100
)

chunks = splitter.split_documents(documents)
print(f'Splitted into {len(chunks)} chunks...')

embeddings = FastEmbedEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.from_documents(chunks,embeddings)

vector_store.save_local("vector_store")
print("Vector STore saved...")