import pandas as pd
from evaluate import load

# Load metrics
bleu = load("bleu")
rouge = load("rouge")
bertscore = load("bertscore")

# Load your CSV
df = pd.read_csv("qa_test_results.csv")  # Columns: question, ground_truth_answer, generated_answer

# Convert to list
references = df['ground_truth_answer'].tolist()
predictions = df['generated_answer'].tolist()

# BLEU
bleu_result = bleu.compute(predictions=predictions, references=[[ref] for ref in references])
print("BLEU Score:", bleu_result['bleu'])

# ROUGE
rouge_result = rouge.compute(predictions=predictions, references=references)
print("ROUGE Scores:", rouge_result)

# BERTScore (Optional – semantic similarity)
bertscore_result = bertscore.compute(predictions=predictions, references=references, lang="en")
print("BERTScore F1:", sum(bertscore_result["f1"]) / len(bertscore_result["f1"]))
