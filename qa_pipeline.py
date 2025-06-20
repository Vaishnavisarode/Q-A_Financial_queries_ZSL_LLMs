
from models.llama_loader import load_llama_model
from transformers import pipeline

# Replace with your actual HF token or fetch from environment
hf_token = "YOUR_TOKEN_HERE"

print("Initializing model and tokenizer...")
model, tokenizer = load_llama_model(hf_token)

qa_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=128,  # instead of max_length
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.1,
)

