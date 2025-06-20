#  Q&A for Financial Queries Using Zero-Shot Learning and Large Language Models (LLMs)

A domain-specific intelligent assistant for answering financial queries using Zero-Shot Learning (ZSL) and state-of-the-art Large Language Models. This project aims to help users—especially entrepreneurs and individuals—make informed financial decisions through a smart, conversational system that doesn't require extensive fine-tuning on new data.

---

##  Project Overview

This project explores the power of **Zero-Shot Learning (ZSL)** and **pretrained LLMs** to address novel financial questions without needing domain-specific fine-tuning. By integrating **LLMs** with financial Q&A datasets like **Finance-Alpaca**, the assistant understands and answers finance-related queries with high relevance.

###  Key Features

-  **Zero-shot inference** for financial questions
-  Support for SIP, EMI, ROI, and budgeting calculations
-  CSV-based financial audit capabilities
-  Hybrid RAG setup using FAISS + Sentence Transformers
-  Intent-based routing for Q&A, calculators, and data audit
-  Powered by models like  LLaMA 2-based LLMs
-  Lightweight, CPU-compatible option for basic setups

---
##  Installation

### 1. Clone this Repository

```bash
git clone https://github.com/Vaishnavisarode/Q-A_Financial_queries_ZSL_LLMs.git

```

### 2. Install Dependencies

```bash
pip -r requirements.txt
```

>  Make sure your Python version is 3.7 or above.

---

##  How It Works

### Intent Classification
Determines if the query is a financial Q&A, calculator request (e.g., SIP), or data audit task.

### Routing
Based on the intent, the query is routed to:

- A retrieval-augmented LLM pipeline

- A financial calculator module

- A CSV analysis module

### Zero-Shot Q&A
If classified as Q&A, it retrieves relevant context from the FAISS store and sends it to the LLM for a final response.

## Models & Technologies Used
- LLMs: LLaMA 2 

- Datasets: Finance-Alpaca

- Vector Store: FAISS

- Embeddings: all-MiniLM-L6-v2 (Sentence Transformers)

- Calculators: Custom SIP/EMI/ROI functions

- ZSL Techniques: Prompt Engineering

## Sample Queries
- "How much will I gain in 5 years if I invest ₹5,000 monthly in a SIP?"

- "What is the EMI for a ₹10L loan at 8.5% for 5 years?"

- "Explain the impact of RBI rate hike on loan borrowers."

- "Analyze this CSV of my expenses and suggest cost-cutting tips."

## Future Improvements
- Add multilingual support (e.g., Hindi, Tamil)

- Enhance calculator module with visualization

- Enable real-time financial news integration

  ## screenshots:
  ### Example of the chatbot interface
  ![Alt Text](Output_images/App_output.jpeg)

  ### Example of module used result
  ![Alt Text](Output_images/Module_used_result.jpeg)

  ### Example of ZSL+RAG result 
  ![Alt Text](Output_images/Result.jpeg)
  
