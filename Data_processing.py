import json
import pandas as pd
import os

file_path = r"C:\Users\nanaw\ZSL\Data\local_datasets\finance_alpaca\finance_alpaca.json"

clean_data = []

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            record = json.loads(line)
            instruction = record.get("instruction", "").strip()
            input_text = record.get("input", "").strip()
            output = record.get("output", "").strip()

            if input_text:
                question = f"{instruction}\n{input_text}"
            else:
                question = instruction

            clean_data.append({"question": question, "answer": output})
        except json.JSONDecodeError as e:
            print("Skipping line due to error:", e)

# Save to CSV
df = pd.DataFrame(clean_data)
df.to_csv("finance_alpaca.csv", index=False)
print("Preprocessing complete. Saved as 'finance_alpaca.csv'")
