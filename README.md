# 💊 Drug Recommendation System – Python + Tableau Dashboard

This project is a healthcare-focused recommendation system that suggests drugs based on either **target diseases** or **active ingredients (contents)**. Built using Python and powered by cosine similarity, it mimics an intelligent layer on top of EMR-like datasets. Additionally, an interactive **BI dashboard** built with **Tableau** provides visual insights into drug usage trends, ingredients, and filterable drug lookup tools.

---

## 📌 Features

### 🔹 Python CLI-Based Recommender

- Recommend drugs based on one or more **diseases**
- Recommend drugs based on **ingredient similarity**
- Uses **cosine similarity** on a binary matrix of diseases or contents
- Accepts **dynamic user input** for flexible recommendation

### 🔹 Tableau Public Dashboard

- Visualize top drugs per disease
- View most commonly used ingredients
- Interactive drug finder based on disease or content
- Easy-to-use filters and tooltips for exploration

👉 **View the dashboard here**:  
[🔗 Tableau Dashboard – Drug Insights Explorer](https://public.tableau.com/app/profile/chethas.anil.reddy/viz/BIDashboardDrugRecommendationsIngredientInsights/DrugRecommendationDashboard?publish=yes)

---

## 🧠 How It Works

### Dataset

- Input: `Drug data.csv`
- Contains three key fields:
  - `drug`: drug name
  - `contents`: comma-separated list of active ingredients
  - `diseases`: comma-separated list of diseases the drug treats

### Python Logic

1. Parses the CSV file
2. Builds a binary matrix of diseases or contents
3. Applies **cosine similarity** to identify drugs with similar treatment profiles
4. Outputs **top 5 recommendations**

---

## 🖥️ How to Run

1. Clone the repo and navigate to the directory:

   ```bash
   git clone https://github.com/ChethasReddy/Drug_recommendation.git

   ```

2. Install Dependencies:

   ```bash
   pip install pandas scikit-learn
   ```

3. Run the script

   ```bash
   python drug_recommendation.py
   ```

4. Input Values when prompted:

Enter disease(s) separated by commas: fever, headache
Enter content(s)/ingredients separated by commas: paracetamol
