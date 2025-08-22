# rag_engine.py
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient
import os

DB_URL = os.environ.get("DB_URL")
RAG_ENGINE_API_KEY = os.environ.get("RAG_ENGINE_API_KEY")
COLLECTION_NAME = "mundial_clubes_2025"

qdrant_client = QdrantClient(url=DB_URL, api_key=RAG_ENGINE_API_KEY)

qdrant = Qdrant(
    client=qdrant_client,
    collection_name=COLLECTION_NAME
)
