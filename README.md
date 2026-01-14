# Mental Health in Tech Analysis 🧠💻

## Project Overview
This project performs an Exploratory Data Analysis (EDA) on the "Mental Health in Tech Survey" dataset. The goal is to identify the key drivers of mental health treatment-seeking behavior in the technology sector and provide data-driven recommendations to improve employee well-being.

Mental health issues are often stigmatized in the workplace. This analysis uncovers the impact of factors like family history, care options, and anonymity on an employee's decision to seek help.

## 📊 Key Insights
* **Family History:** The strongest predictor of seeking treatment. Employees with a family history of mental illness are nearly **2x more likely** to seek help.
* **Awareness Matters:** Employees who *know* about their employer's care options are significantly more likely to seek treatment compared to those who are "Not sure."
* **Geography:** The United States and Australia have much higher reported treatment rates (~60%) compared to many European countries (~30-40%).
* **Stigma:** A "Fear Factor" exists. Employees who believe there are negative consequences for discussing mental health are less likely to seek help.

## 📂 Dataset
The dataset consists of **1,259 responses** from tech workers.
* **Source:** [OSMI Mental Health in Tech Survey](https://www.kaggle.com/osmi/mental-health-in-tech-survey) (or "Uploaded survey.csv" in this repo).
* **Key Variables:**
    * `treatment` (Target): Has the employee sought treatment?
    * `family_history`: Family history of mental illness.
    * `care_options`: Knowledge of employer-provided care options.
    * `work_interfere`: Does mental health interfere with work?
    * `anonymity`: Is anonymity protected?

## 🛠️ Tools & Technologies
* **Python:** The core programming language.
* **Pandas:** For data manipulation and cleaning.
* **Matplotlib & Seaborn:** For data visualization and charting.
* **Scikit-Learn:** For Label Encoding to calculate correlations.
* **Jupyter Notebook:** The interactive environment used for the analysis.

## 🚀 How to Run this Project
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Mental-Health-Tech-Analysis.git](https://github.com/YOUR_USERNAME/Mental-Health-Tech-Analysis.git)
    ```
2.  **Install dependencies:**
    You will need Python installed. Then run:
    ```bash
    pip install pandas numpy seaborn matplotlib scikit-learn
    ```
3.  **Run the Notebook:**
    Open `Sample_EDA_Submission_Template.ipynb` in Jupyter Notebook, Google Colab, or VS Code and run all cells.

## 📈 Visualizations
The project includes over 20 visualizations, including:
* **Correlation Heatmap:** To identify top predictors.
* **Stacked Bar Charts:** For geographic and categorical comparisons.
* **Pair Plots:** To visualize complex relationships between age, history, and treatment.

## 💡 Business Recommendations
Based on the analysis, the following actions are recommended for employers:
1.  **Launch an Awareness Campaign:** Actively communicate available care options to convert "Don't know" responses into "Yes."
2.  **Early Screening:** Offer confidential screenings, especially for high-risk groups (those with family history).
3.  **Guarantee Anonymity:** Explicitly state in policy that seeking help is confidential to reduce stigma.



---
*This project was completed as part of a Data Science Capstone/EDA Project.*
