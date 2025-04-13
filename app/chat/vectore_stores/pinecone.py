import os 
import pinecone
from langchain.vectorstores.pinecone import Pinecone
from app.chat.embeddings.openai import embeddings

# Initialize Pinecone
pinecone.Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV_NAME")
)

# Index name

vector_store = Pinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"),embeddings
)

def build_retriever(chat_arg):
    """Builds a retriever from the vector store."""
    search_kwargs = {
        "filter": {"pdf_id":chat_arg.pdf_id},
    }
    return vector_store.as_retriever(search_kwargs=search_kwargs)