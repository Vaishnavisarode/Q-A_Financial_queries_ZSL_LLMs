
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from models.llama_loader import load_llama_model
import os

hf_token = "YOUR_TOKEN_HERE"

# Load FAISS index and docs
index_path = os.path.join("Data", "finance_index.faiss")
index = faiss.read_index(index_path)
with open(os.path.join("Data", "finance_documents.pkl"), "rb") as f:
    documents = pickle.load(f)



# Load embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

model = None
tokenizer = None
qa_pipeline = None

def retrieve_and_answer(query: str) -> str:
    global model, tokenizer, qa_pipeline

    # Step 1: Vectorize query
    query_vec = embedder.encode([query])
    
    # Step 2: Search FAISS
    top_k = 3
    distances, indices = index.search(np.array(query_vec), top_k)
    context = "\n---\n".join([documents[i] for i in indices[0]])

    # Step 3: Build prompt
    prompt = f"""
    Answer the following financial question using the provided context. Be brief, helpful, and specific.

    Context:
    {context}

    Question: {query}
    Answer:
    """

    # Step 4: Generate answer
    if qa_pipeline is None:
        model, tokenizer = load_llama_model(hf_token)
        qa_pipeline = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=128,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.1,
        )

    # outputs = qa_pipeline(prompt)
    # return outputs[0]["generated_text"]
    outputs = qa_pipeline(prompt)
    full_text = outputs[0]["generated_text"]

    # Remove the prompt from the beginning, get only the answer part
    answer = full_text[len(prompt):].strip()

    return answer
