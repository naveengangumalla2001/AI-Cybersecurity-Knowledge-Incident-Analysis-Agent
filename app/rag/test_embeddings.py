from app.rag.embeddings import get_embeddings


embeddings = get_embeddings()

text = "A large number of failed login attempts may indicate a brute force attack."

vector = embeddings.embed_query(text)

print("\nEmbedding created successfully!")

print("Vector type:", type(vector))
print("Vector dimensions:", len(vector))

print("\nFirst 10 values:")
print(vector[:10])