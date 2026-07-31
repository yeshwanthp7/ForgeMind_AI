from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text):
    """
    Convert text into an embedding vector.
    """
    embedding = model.encode(text)
    return embedding


# Test
if __name__ == "__main__":
    sample_text = "Machine temperature exceeded safe limit."

    vector = generate_embedding(sample_text)

    print("Embedding Generated Successfully!")
    print("Vector Length:", len(vector))