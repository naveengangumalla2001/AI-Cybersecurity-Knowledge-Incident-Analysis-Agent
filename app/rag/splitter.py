from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.rag.loader import load_documents


def split_documents():

    documents = load_documents()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(documents)

    return chunks