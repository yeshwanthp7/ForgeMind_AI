from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read knowledge file
with open("knowledge.txt", "r", encoding="utf-8") as f:
    documents = f.readlines()

documents = [doc.strip() for doc in documents if doc.strip()]

# Create embeddings
embeddings = model.encode(documents)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# User query
query = "Why is the machine overheating?"

# Convert query to embedding
query_embedding = model.encode([query])

# Search
distance, indices = index.search(np.array(query_embedding), k=1)

print("User Query:", query)
print("Most Relevant Result:", documents[indices[0][0]])

def search_rag(query):
    query_embedding = model.encode([query])
    distance, indices = index.search(np.array(query_embedding), k=1)
    return documents[indices[0][0]]