from intent_classifier import classify_intent
from calc_module import handle_calc
from analysis_module import handle_csv_audit
from retriever import retrieve_and_answer

def main():
    print("\n Welcome to the Financial Q&A Assistant (ZSL + RAG powered)")
    print("-------------------------------------------------------------")
    print("Type your financial question (or type 'exit' to quit):\n")

    while True:
        query = input(" You: ")

        if query.lower() in ["exit", "quit"]:
            print(" Goodbye!")
            break
        answer = generate_answer(query)
        print(f"\n Assistant: {answer}")

def generate_answer(query: str) -> str:
    intent = classify_intent(query)

    if intent == "calculator":
        return handle_calc(query)
    elif intent == "audit":
        return handle_csv_audit(query)
    else:
        try:
            return retrieve_and_answer(query)
        except Exception as e:
            return f"Error answering your question: {e}"

if __name__ == "__main__":
    main()
