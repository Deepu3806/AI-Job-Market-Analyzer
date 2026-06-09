import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_data_analyst_jobs.csv")

print("========== DATASET OVERVIEW ==========")
print(df.head())

# ==========================================
# TOP JOB TITLES
# ==========================================

print("\n========== TOP JOB TITLES ==========\n")
print(df['Job Title'].value_counts().head(10))

# ==========================================
# TOP LOCATIONS
# ==========================================

print("\n========== TOP LOCATIONS ==========\n")
print(df['Location'].value_counts().head(10))

# ==========================================
# TOP COMPANIES
# ==========================================

print("\n========== TOP COMPANIES ==========\n")
print(df['Company Name'].value_counts().head(10))

# ==========================================
# TOP INDUSTRIES
# ==========================================

print("\n========== TOP INDUSTRIES ==========\n")
print(df['Industry'].value_counts().head(10))

# ==========================================
# COMPANY RATINGS
# ==========================================

print("\n========== COMPANY RATINGS ==========\n")
print(df['Rating'].describe())

print("\n🎉 Exploratory Data Analysis Completed!")