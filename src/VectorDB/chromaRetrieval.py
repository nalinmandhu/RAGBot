from sentence_transformers import SentenceTransformer
import os
import chromadb
from dotenv import load_dotenv

load_dotenv()
EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL")
model = SentenceTransformer(EMBEDDING_MODEL)
DOCS_FOLDER = r"..\demo_bot_data"
DB_PATH = r"..\chromadb_store"

#Initialize ChromaDB client
client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection(name="ubuntu_docs")


def query_docs(query_text, top_k=5):
    query_embedding = model.encode(query_text).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    metadatas = results.get("metadatas", [[]])[0]
    return [metadata.get("content", "") for metadata in metadatas]



