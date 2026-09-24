import os
from dotenv import load_dotenv

load_dotenv()

_chain = None


def get_chain():
    global _chain

    if _chain is not None:
        return _chain

    from pinecone import Pinecone
    from langchain_groq import ChatGroq
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser

    pc = Pinecone(
        api_key=os.getenv("PINECONE_API_KEY")
    )

    index = pc.Index(
        os.getenv("PINECONE_INDEX_NAME")
    )

    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model_name="openai/gpt-oss-120b"
    )

    prompt = ChatPromptTemplate.from_template("""
You are RON, a personal AI assistant on Mohammad Awez Haider's portfolio website.

Answer questions about Haider's skills, projects, experience, and background in a concise manner.
Try to break the responses into different lines instead of a single paragraph.
Be professional, concise, and confident.
If you don't know something, say so honestly.
Never make up information.
Always use all the context provided to give a complete answer.

Context:
{context}

Question:
{question}

Answer:
""")

    parser = StrOutputParser()

    def ask_ron(question):
        results = index.search(
            namespace="portfolio",
            query={
                "inputs": {
                    "text": question
                },
                "top_k": 5
            },
            fields=["text", "source"]
        )

        docs = results["result"]["hits"]

        context = "\n\n".join(
            doc["fields"]["text"]
            for doc in docs
        )

        chain = prompt | llm | parser

        return chain.invoke({
            "context": context,
            "question": question
        })

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