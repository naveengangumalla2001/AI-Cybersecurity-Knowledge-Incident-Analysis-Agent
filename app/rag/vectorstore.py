from pathlib import Path

from langchain_community.vectorstores import FAISS

from app.rag.splitter import split_documents
from app.rag.embeddings import get_embeddings


# --------------------------------------------------
# Vector Database Path
# --------------------------------------------------

VECTORSTORE_PATH = Path("data/vectorstore")

FAISS_INDEX_FILE = VECTORSTORE_PATH / "index.faiss"
FAISS_PICKLE_FILE = VECTORSTORE_PATH / "index.pkl"


# --------------------------------------------------
# Create Vector Database
# --------------------------------------------------

def create_vectorstore():

    print("\nCreating vector database...")

    # Load and split documents
    chunks = split_documents()

    print(f"Total chunks created: {len(chunks)}")

    # Load embedding model
    embeddings = get_embeddings()

    # Create FAISS vector database
    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    # Create folder if it doesn't exist
    VECTORSTORE_PATH.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save FAISS database
    vectorstore.save_local(
        str(VECTORSTORE_PATH)
    )

    print("\nVector database created successfully!")
    print(f"Saved at: {VECTORSTORE_PATH}")

    return vectorstore


# --------------------------------------------------
# Load Existing Vector Database
# --------------------------------------------------

def load_vectorstore():

    # Check whether both FAISS files exist
    if (
        FAISS_INDEX_FILE.exists()
        and FAISS_PICKLE_FILE.exists()
    ):

        print("\nLoading existing vector database...")

        embeddings = get_embeddings()

        vectorstore = FAISS.load_local(
            str(VECTORSTORE_PATH),
            embeddings,
            allow_dangerous_deserialization=True
        )

        print("Vector database loaded successfully!")

        return vectorstore

    # If files do not exist, create database
    print("\nVector database not found.")

    return create_vectorstore()