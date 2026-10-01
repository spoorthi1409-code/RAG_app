from sentence_transformers import SentenceTransformer
with open("fest_info.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(f"Your file has {len(text)} characters.")
print()
print("Sample text:", text[:300])

# Function to create chunks
def chunk_text(text, chunk_size=300, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap
    return chunks

# Create chunks
chunks = chunk_text(text)
print(f"Total chunks created: {len(chunks)}")

# Load Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(chunks)
print(f"Shape of embeddings: {embeddings.shape}")
# Display first 5 values of each embedding
for i in range(len(embeddings)):
    print(f"Embedding_{i+1}: {embeddings[i][:5]}")
    print()
    print("----------------------------------------")

# Display chunks if needed
# for i in range(len(chunks)):
#     print(f"Chunk_{i+1}: {chunks[i]}")
#     print()
#     print("----------------------------------------")

question = "What is the cost of registration?"
q_embedding = model.encode([question]).tolist()

results = collection.query(query_embeddings=q_embedding, n_results=1)
retrieved=results["documents"][0]
print(retrieved)
