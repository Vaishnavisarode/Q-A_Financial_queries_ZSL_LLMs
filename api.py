
from fastapi import FastAPI, Request, UploadFile, File, Form
from pydantic import BaseModel
from retriever import retrieve_and_answer as retrieve_relevant_docs
from main import generate_answer  # Your LLM + RAG pipeline
from analysis_module import handle_csv_audit
from fastapi.middleware.cors import CORSMiddleware
import io
import pandas as pd
import shutil
import tempfile


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

uploaded_file_path = "uploaded.csv"

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    contents = await file.read()
    with open(uploaded_file_path, "wb") as f:
        f.write(contents)
    return {"message": "CSV uploaded successfully"}

@app.post("/ask")
async def ask_query(payload: dict):
    query = payload.get("query", "")

    if "csv" in query.lower() or "audit" in query.lower():
        try:
            raw_audit = handle_csv_audit(uploaded_file_path, query)
            # Refine audit result using LLM
            final_response = generate_answer(f"Audit result: {raw_audit}\nExplain in detail.")
            return {"answer": final_response}
        except Exception as e:
            return {"error": f"CSV audit failed: {str(e)}"}

    # Else, use RAG
    try:
        rag_response = generate_answer(query)
        return {"answer": rag_response}
    except:
        fallback = generate_answer(query)
        return {"answer": fallback}
