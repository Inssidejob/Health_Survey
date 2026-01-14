import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
from sklearn.preprocessing import LabelEncoder

# 1. Setup Visuals
sns.set(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (10, 6)

# 2. Load Data
df = pd.read_csv('survey.csv')

# 3. Clean Gender (Standardizing 40+ spellings)
def clean_gender(gender):
    gender = str(gender).lower().strip()
    if gender in ['male', 'm', 'male-ish', 'maile', 'cis male', 'mal', 'man', 'cis man', 'make', 'mail']:
        return 'Male'
    elif gender in ['female', 'cis female', 'f', 'woman', 'femake', 'female (cis)', 'cis-female/femme']:
        return 'Female'
    else:
        return 'Other'

df['Gender'] = df['Gender'].apply(clean_gender)

# 4. Clean Age (Removing outliers)
df = df[(df['Age'] >= 18) & (df['Age'] <= 100)]

# 5. Handle Missing Values
df['work_interfere'] = df['work_interfere'].fillna('Unknown')
df['self_employed'] = df['self_employed'].fillna('No')

print("Data Loaded and Cleaned Successfully.")


def plot_dynamic_grid(dataframe, columns_list, plot_type='count', hue=None):
    """
    Creates a grid of charts automatically based on the list of columns passed.
    """
    num_plots = len(columns_list)
    cols = 3  # Number of columns in the grid
    rows = math.ceil(num_plots / cols)

    # Create the figure with dynamic height
    fig, axes = plt.subplots(rows, cols, figsize=(18, rows * 5))
    axes = axes.flatten()  # Flatten 2D grid to 1D list

    for i, col in enumerate(columns_list):
        # Logic for Categorical plots
        if plot_type == 'count':
            # Check if too many unique values (like Country), rotate labels if so
            if dataframe[col].nunique() > 10:
                rotation = 90
            else:
                rotation = 45

            sns.countplot(x=col, data=dataframe, ax=axes[i], hue=hue)
            axes[i].tick_params(axis='x', rotation=rotation)

        # Logic for Numerical plots
        elif plot_type == 'hist':
            sns.histplot(dataframe[col], kde=True, ax=axes[i], color='teal')

        axes[i].set_title(f'Distribution of {col}')

    # Hide any empty subplot slots (e.g. if you asked for 5 plots in a 3x2 grid)
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

# LIST 1: Workplace Culture Variables
# We want to see how these affect treatment, so we add hue='treatment'
workplace_vars = ['work_interfere', 'benefits', 'care_options', 'wellness_program', 'seek_help', 'anonymity', 'leave']

print("--- Workplace Culture & Treatment ---")
plot_dynamic_grid(df, workplace_vars, plot_type='count', hue='treatment')

# LIST 2: Demographics
# Just simple distributions
demo_vars = ['Gender', 'remote_work', 'tech_company', 'family_history']

print("--- Demographics Overview ---")
plot_dynamic_grid(df, demo_vars, plot_type='count')

# Question: How does mental health vary by Location?

# Filter for top 10 countries to keep chart readable
top_countries = df['Country'].value_counts().iloc[:10].index
df_geo = df[df['Country'].isin(top_countries)]

# Calculate Percentages
geo_treatment = df_geo.groupby('Country')['treatment'].value_counts(normalize=True).unstack()
geo_treatment = geo_treatment.sort_values(by='Yes')

# Plot Stacked Bar
geo_treatment.plot(kind='barh', stacked=True, color=['skyblue', 'orange'], figsize=(12, 8))
plt.title('Percentage of Employees Seeking Treatment by Country (Top 10)')
plt.xlabel('Proportion')
plt.legend(title='Sought Treatment', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Question: What are the strongest predictors?

# 1. Encode text to numbers
le = LabelEncoder()
df_encoded = df.copy()
for col in df_encoded.columns:
    if df_encoded[col].dtype == 'object':
        df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))

# 2. Plot Heatmap focusing on 'treatment'
plt.figure(figsize=(10, 8))
# Sort by correlation strength
heatmap_data = df_encoded.corr()[['treatment']].sort_values(by='treatment', ascending=False)
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation of Variables with Seeking Treatment')
plt.show()

# 3. Print the top answer
print("Top 3 Predictors:")
print(heatmap_data.head(4)) # Top 3 + Treatment itself

# --- CHART 14: MENTAL VS PHYSICAL HEALTH IMPORTANCE ---
plt.figure(figsize=(10, 6))

sns.countplot(x='mental_vs_physical', hue='treatment', data=df, order=['Yes', 'No', "Don't know"])
plt.title('Does Employer Take Mental Health as Seriously as Physical Health?')
plt.xlabel('Perceived Employer Attitude')
plt.legend(title='Sought Treatment')
plt.show()

# --- CHART 15: OBSERVED CONSEQUENCES ---
plt.figure(figsize=(10, 6))

sns.countplot(x='obs_consequence', hue='treatment', data=df)
plt.title('Have you heard of negative consequences for coworkers with mental health conditions?')
plt.xlabel('Observed Negative Consequences')
plt.legend(title='Sought Treatment')
plt.show()