from app.rag.vectorstore import create_vectorstore


vectorstore = create_vectorstore()

print("\nVector database created successfully!")

print("Number of vectors:", vectorstore.index.ntotal)