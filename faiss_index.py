
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os

# Path to your processed CSV
csv_path =  r"C:\Users\nanaw\ZSL\Data\finance_alpaca.csv"  # Make sure this file exists

# Load dataset
df = pd.read_csv(csv_path)

# Clean NaNs or floats
df = df.dropna(subset=["question", "answer"])
df["question"] = df["question"].astype(str).str.strip()
df["answer"] = df["answer"].astype(str).str.strip()

# Build documents list (Q&A pairs)
documents = []
for _, row in df.iterrows():
    question = row["question"]
    answer = row["answer"]
    text = f"Q: {question}\nA: {answer}"
    documents.append(text)

print(f"Total documents prepared: {len(documents)}")

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

print("Embedding documents...")
embeddings = model.encode(documents, show_progress_bar=True, convert_to_numpy=True)

# Create FAISS index
embedding_dim = embeddings.shape[1]
index = faiss.IndexFlatL2(embedding_dim)
index.add(embeddings)

print(f"FAISS index created with {index.ntotal} vectors (dimension={embedding_dim})")

# Save index and documents
os.makedirs("Data", exist_ok=True)

faiss.write_index(index, "Data/finance_index.faiss")
with open("Data/finance_documents.pkl", "wb") as f:
    pickle.dump(documents, f)

print("Saved FAISS index and documents to 'Data/' folder.")
