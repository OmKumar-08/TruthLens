import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.storage import LocalFileStore
from langchain_core.documents import Document


load_dotenv()

persist_directory = "./chroma_db"


embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


def get_vectorstore():
    return Chroma(persist_directory=persist_directory, embedding_function=embed_model)


def add_documents_to_chroma(texts, metadatas=None):
    vectorstore = get_vectorstore()
    vectorstore.add_texts(texts, metadatas=metadatas)
    vectorstore.persist()


def search_chroma(query: str, top_k: int = 3):
    vectorstore = get_vectorstore()
    docs = vectorstore.similarity_search(query, k=top_k)
    return [doc.page_content for doc in docs]


def add_to_vectorstore(texts: list[str], metadatas: list[dict] = None):
    vectorstore = get_vectorstore()
    documents = [Document(page_content=text, metadata=meta or {}) for text, meta in zip(texts, metadatas or [{}]*len(texts))]
    vectorstore.add_documents(documents)
    vectorstore.persist()
