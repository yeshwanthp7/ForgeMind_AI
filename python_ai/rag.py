import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample incident reports
documents = [
    "Boiler temperature exceeded safe limit.",
    "Pump pressure dropped suddenly.",
    "Gas leakage detected near storage tank.",
    "Cooling system failure caused overheating."
]

# Create embeddings
embeddings = model.encode(documents)

# Convert to NumPy array
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def search_incident(query):
    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, 1)

    return documents[indices[0][0]]

# Test
if __name__ == "__main__":
    query = "Machine is getting too hot."

    result = search_incident(query)

    print("Most Similar Incident:")
    print(result)