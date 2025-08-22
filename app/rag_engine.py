# rag_engine.py
from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient
from langchain.embeddings.openai import OpenAIEmbeddings
import os

DB_URL = os.environ.get("DB_URL")
RAG_ENGINE_API_KEY = os.environ.get("RAG_ENGINE_API_KEY")
COLLECTION_NAME = "mundial_clubes_2025"

# Cliente Qdrant
qdrant_client = QdrantClient(url=DB_URL, api_key=RAG_ENGINE_API_KEY)

# Inicializamos embeddings
embeddings = OpenAIEmbeddings()  # o la clase de embeddings que uses

# Vector store
qdrant = Qdrant(
    client=qdrant_client,
    collection_name=COLLECTION_NAME,
    embeddings=embeddings
)
