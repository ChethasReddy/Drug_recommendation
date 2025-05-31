import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv("Drug data.csv")[['drug', 'contents', 'diseases']].fillna("")

# --- Recommendation Based on Disease ---

print('\n=== Drug Recommendation Based on Disease ===\n')


user_disease_input = input("Enter disease(s) separated by commas: ").strip().lower()
target_diseases = [d.strip() for d in user_disease_input.split(',') if d.strip()]
print(f"\nFinding drug recommendations for diseases: {target_diseases}\n")


parsed_diseases = []
for disease_str in df['diseases']:
    diseases = [d.strip().lower() for d in str(disease_str).split(',') if d.strip()]
    parsed_diseases.append(diseases)


disease_matrix = [
    [1 if disease in drug_diseases else 0 for disease in target_diseases]
    for drug_diseases in parsed_diseases
]


disease_sim = cosine_similarity(disease_matrix)
disease_scores = pd.Series(disease_sim.sum(axis=1)).sort_values(ascending=False)
top_disease_drugs = df['drug'].iloc[disease_scores.index[:5]].tolist()

print("Top 5 drug recommendations based on disease:")
print(top_disease_drugs)

# --- Recommendation Based on Contents ---

print('\n=== Drug Recommendation Based on Contents ===\n')


user_content_input = input("Enter content(s)/ingredients separated by commas: ").strip().lower()
target_contents = [c.strip() for c in user_content_input.split(',') if c.strip()]
print(f"\nFinding drug recommendations for contents: {target_contents}\n")


parsed_contents = []
for content_str in df['contents']:
    contents = [c.strip().lower() for c in str(content_str).split(',') if c.strip()]
    parsed_contents.append(contents)


content_matrix = [
    [1 if content in drug_contents else 0 for content in target_contents]
    for drug_contents in parsed_contents
]


content_sim = cosine_similarity(content_matrix)
content_scores = pd.Series(content_sim.sum(axis=1)).sort_values(ascending=False)
top_content_drugs = df['drug'].iloc[content_scores.index[:5]].tolist()

print("Top 5 drug recommendations based on contents:")
print(top_content_drugs)
