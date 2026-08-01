from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


def create_chunks(knowledge):

    # ================= CHUNKING MODULE =================

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_text(knowledge)

    print("\n===== CHUNKING MODULE =====")
    print("Total Chunks Created:", len(chunks))

    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i+1}:")
        print(chunk[:200])

    return chunks



def create_embeddings(chunks):

    # ================= EMBEDDING MODULE =================

    print("\n===== EMBEDDING MODULE =====")

    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = model.encode(chunks)

    print("Embeddings Created Successfully")
    print("Embedding Shape:", embeddings.shape)

    # ================= VECTOR DATABASE =================

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    print("FAISS Vector Database Created Successfully")

    return model, index, embeddings

import os
from huggingface_hub import login 
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
print("HF_TOKEN:", os.getenv("HF_TOKEN"))
token = os.getenv("HF_TOKEN")
if token:
    login(token=token)
model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    "Machine temperature is very high.",
    "Pressure exceeds safety limit.",
    "Cooling fan is not working."
]

# Create embeddings
embeddings = model.encode(texts)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings
index.add(np.array(embeddings))

print("Embeddings created successfully!")
print("Total vectors:", index.ntotal)