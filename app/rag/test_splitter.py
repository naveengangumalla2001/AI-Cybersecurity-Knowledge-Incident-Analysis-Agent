from app.rag.splitter import split_documents


chunks = split_documents()

print(f"\nTotal chunks created: {len(chunks)}")

for i, chunk in enumerate(chunks):

    print("\n==============================")
    print(f"Chunk {i + 1}")
    print("==============================")

    print("Source:", chunk.metadata.get("source"))

    print("\nContent:")
    print(chunk.page_content)

    print("\nChunk length:", len(chunk.page_content))