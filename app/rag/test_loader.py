from app.rag.loader import load_documents


documents = load_documents()

print(f"\nTotal documents loaded: {len(documents)}")

for i, document in enumerate(documents):

    print("\n==============================")
    print(f"Document {i + 1}")
    print("==============================")

    print("Source:", document.metadata.get("source"))

    print("\nContent:")
    print(document.page_content[:500])