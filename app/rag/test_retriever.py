from app.rag.retriever import get_retriever


retriever = get_retriever()

query = """
A web server received thousands of failed login
attempts from multiple IP addresses.
"""

documents = retriever.invoke(query)

print("\nRetrieved documents:", len(documents))

for i, document in enumerate(documents):

    print("\n==============================")
    print(f"Result {i + 1}")
    print("==============================")

    print("Source:", document.metadata.get("source"))

    print("\nContent:")
    print(document.page_content)