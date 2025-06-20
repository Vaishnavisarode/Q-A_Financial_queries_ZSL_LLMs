
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

def load_llama_model(hf_token):
    model_name = "meta-llama/Llama-2-7b-chat-hf"

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True, token=hf_token)
    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        token=hf_token,
        quantization_config=bnb_config,
        device_map={"": 0},
        trust_remote_code=True
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name, token=hf_token)

    return model, tokenizer

if __name__ == "__main__":
    from getpass import getpass
    
    # Optional: prompt for Hugging Face token securely
    hf_token = getpass("Enter your Hugging Face token: ")  # or paste your token directly for testing
    
    # Call your function
    try:
        model, tokenizer = load_llama_model(hf_token)
        print("✅ Model and tokenizer loaded successfully!")
        
        # Optional: test a small inference
        input_text = "Explain the concept of compound interest."
        inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
        output = model.generate(**inputs, max_new_tokens=100)
        print("🧠 Output:\n", tokenizer.decode(output[0], skip_special_tokens=True))

    except Exception as e:
        print(" Error occurred during model loading or inference:\n", e)
