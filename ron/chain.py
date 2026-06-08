import os
from dotenv import load_dotenv
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Load everything once
embeddings = FastEmbedEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.load_local(
    "vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

prompt = ChatPromptTemplate.from_template("""
You are RON, a personal AI assistant on Mohammad Awez Haider's portfolio website.
Answer questions about Haider's skills, projects, experience, and background.
Be professional, concise, and confident. If you don't know something, say so honestly.
Never make up information.

Context:
{context}

Question:
{question}

Answer:""")

parser = StrOutputParser()

def ask_ron(question):
    docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in docs)
    chain = prompt | llm | parser
    return chain.invoke({"context": context, "question": question})


# Test
if __name__ == "__main__":
    questions = [
        "What projects has Haider worked on?",
        "What is Haider's CGPA?",
        "What is Aquelious?",
        "Is Haider available for internships?",
    ]
    for q in questions:
        print(f"\nQ: {q}")
        print(f"RON: {ask_ron(q)}")