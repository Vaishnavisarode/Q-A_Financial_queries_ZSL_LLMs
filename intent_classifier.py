
def classify_intent(query: str) -> str:
    query = query.lower().strip()

    # Keywords that indicate the user is asking for a **calculation**
    calc_keywords = [
        "calculate", "how much", "expected", "amount", "monthly", "emi of", 
        "sip amount", "roi of", "investment return", "total return", "future value"
    ]

    # Keywords for **CSV audit** intent
    audit_keywords = ["upload", "analyze", "audit", "csv", "statement", "summary"]

    # Check for calculator-related query
    if any(kw in query for kw in calc_keywords):
        return "calculator"

    # Check for audit-related query
    if any(kw in query for kw in audit_keywords):
        return "audit"

    # Default case: Assume it is a knowledge or conceptual/comparative query
    return "qna"


