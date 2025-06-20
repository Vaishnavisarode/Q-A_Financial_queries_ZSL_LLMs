
from qa_pipeline import qa_pipeline

def handle_csv_audit(query: str) -> str:
    prompt = f"""You are a financial audit expert. Based on the following user task or file mention, explain what can be audited, what anomalies might be detected, and what actionable insights might be found.

Request: {query}

Audit Summary:"""

    response = qa_pipeline(prompt)[0]["generated_text"].split("Audit Summary:")[-1].strip()
    return f" Audit Insight: {response}"

