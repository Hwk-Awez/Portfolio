import os
from dotenv import load_dotenv

load_dotenv()

_chain = None

def get_chain():
    global _chain
    if _chain is not None:
        return _chain

    from langchain_community.vectorstores import FAISS
    from langchain_huggingface import HuggingFaceEndpointEmbeddings
    from langchain_groq import ChatGroq
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser

    embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_TOKEN")
)
    vectorstore = FAISS.load_local(
        "vector_store",
        embeddings,
        allow_dangerous_deserialization=True
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"
    )
    prompt = ChatPromptTemplate.from_template("""
You are RON, a personal AI assistant on Mohammad Awez Haider's portfolio website.
Answer questions about Haider's skills, projects, experience, and background in a concise manner, like point wise.
Be professional, concise, and confident. If you don't know something, say so honestly.
Never make up information. Always use all the context provided to give a complete answer.

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

    _chain = ask_ron
    return _chain


def ask_ron(question):
    return get_chain()(question)

if __name__ == "__main__":
    questions = [
        "What projects has Haider worked on?",
        "What is Haider's CGPA?",
    ]
    for q in questions:
        print(f"\nQ: {q}")
        print(f"RON: {ask_ron(q)}")