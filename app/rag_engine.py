import os
from langchain.vectorstores import Qdrant
from langchain.embeddings import HuggingFaceEmbeddings
from qdrant_client import QdrantClient

DB_URL = os.environ.get("DB_URL")
RAG_ENGINE_API_KEY = os.environ.get("RAG_ENGINE_API_KEY")
COLLECTION_NAME = "mundial_clubes_2025"

# Connect to Qdrant
qdrant_client = QdrantClient(
    url=DB_URL,
    api_key=RAG_ENGINE_API_KEY
)

# Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create Qdrant vectorstore
qdrant = Qdrant.from_documents(
    documents=[],  # aquí puedes pasar los chunks si quieres poblarlo
    embedding=embeddings,
    collection_name=COLLECTION_NAME,
    client=qdrant_client  # ⚠️ usa 'client' en lugar de location/api_key
)
