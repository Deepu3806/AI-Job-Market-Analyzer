import pandas as pd

# ==========================================
# STEP 1: LOAD THE DATASET
# ==========================================

try:
    df = pd.read_csv("DataAnalyst.csv")
    print("✅ Dataset Loaded Successfully!\n")

except FileNotFoundError:
    print("❌ ERROR: DataAnalyst.csv file not found!")
    print("Make sure DataAnalyst.csv is in the same folder as this script.")
    exit()

# ==========================================
# STEP 2: SHOW BASIC INFORMATION
# ==========================================

print("========== FIRST 5 ROWS ==========\n")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns)

# ==========================================
# STEP 3: REMOVE DUPLICATES
# ==========================================

before_duplicates = df.shape[0]

df.drop_duplicates(inplace=True)

after_duplicates = df.shape[0]

print(f"\n✅ Removed {before_duplicates - after_duplicates} duplicate rows")

# ==========================================
# STEP 4: REMOVE UNNECESSARY COLUMNS
# ==========================================

if "Unnamed: 0" in df.columns:
    df.drop("Unnamed: 0", axis=1, inplace=True)
    print("✅ Removed column: Unnamed: 0")

# ==========================================
# STEP 5: HANDLE MISSING VALUES
# ==========================================

# Replace -1 with NaN
df.replace(-1, pd.NA, inplace=True)

print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())

# ==========================================
# STEP 6: CLEAN COMPANY NAME COLUMN
# ==========================================

if "Company Name" in df.columns:

    # Remove extra spaces
    df["Company Name"] = df["Company Name"].astype(str).str.strip()

    # Remove ratings accidentally attached with company names
    df["Company Name"] = df["Company Name"].str.split("\n").str[0]

    print("\n✅ Company Name column cleaned")

# ==========================================
# STEP 7: CLEAN SALARY COLUMN
# ==========================================

if "Salary Estimate" in df.columns:

    df["Salary Estimate"] = (
        df["Salary Estimate"]
        .astype(str)
        .str.replace(r"\(Glassdoor est\.\)", "", regex=True)
        .str.replace(r"\$", "", regex=True)
        .str.replace(r"K", "", regex=True)
        .str.strip()
    )

    print("✅ Salary Estimate column cleaned")

# ==========================================
# STEP 8: CLEAN LOCATION COLUMN
# ==========================================

if "Location" in df.columns:

    df["Location"] = df["Location"].astype(str).str.strip()

    print("✅ Location column cleaned")

# ==========================================
# STEP 9: SAVE CLEANED FILES
# ==========================================

# Save cleaned CSV
df.to_csv("cleaned_data_analyst_jobs.csv", index=False)

# Save cleaned Excel file
df.to_excel("cleaned_data_analyst_jobs.xlsx", index=False)

print("\n✅ Cleaned files saved successfully!")

print("\nCreated Files:")
print("1. cleaned_data_analyst_jobs.csv")
print("2. cleaned_data_analyst_jobs.xlsx")

# ==========================================
# STEP 10: FINAL DATASET INFO
# ==========================================

print("\n========== FINAL DATASET SHAPE ==========")
print(df.shape)

print("\n🎉 DATA CLEANING COMPLETED SUCCESSFULLY!")