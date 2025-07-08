
# ----------------------------------------
# Create Sample Messy CSV File (One-Time Setup)
# ----------------------------------------

with open("messy_scores.csv", "w") as f:
    f.write("""Name,Score
Alice,85
Bob,
Charlie,78
bob,90
David,   92
Eve,NaN
Frank,88
Grace,not_available
Alice,85
Hannah,72
""")


# ----------------------------------------
# Importing Pandas and Reading Messy Data
# ----------------------------------------

import pandas as pd

# Load the messy_scores.csv dataset
df = pd.read_csv("messy_scores.csv")
print(df.head())        # Preview first 5 rows
print(df.info())        # Check data types and non-null counts

# ----------------------------------------
# Initial Exploration and Validation
# ----------------------------------------

print(df.isnull().sum())        # Count missing values in each column
print(df["Score"].unique())     # View unique values in Score column
print(df.dtypes)                # Check column data types
print(df.duplicated().sum())    # Count duplicate rows

# ----------------------------------------
# Cleaning Step 1: Replace Invalid Placeholders
# ----------------------------------------

# Convert 'not_available' strings to actual missing values
df["Score"].replace("not_available", pd.NA, inplace=True)

# ----------------------------------------
# Cleaning Step 2: Handle Missing Values
# ----------------------------------------

# Option A: Fill missing values with 0
df["Score"].fillna(0, inplace=True)

# Option B: Fill missing values with the average score
avg = df["Score"].mean()
df["Score"].fillna(avg, inplace=True)

# Option C: Drop rows with any missing values
df.dropna(inplace=True)

# ----------------------------------------
# Cleaning Step 3: Fix Data Types
# ----------------------------------------

# Convert Score column to numeric type
df["Score"] = pd.to_numeric(df["Score"], errors="coerce")

# ----------------------------------------
# Cleaning Step 4: Remove Duplicates
# ----------------------------------------

df.drop_duplicates(inplace=True)

# Optional: Remove duplicates based on Name only
df.drop_duplicates(subset="Name", inplace=True)

# ----------------------------------------
# Cleaning Step 5: Standardize Text Format
# ----------------------------------------

# Strip spaces and capitalize names
df["Name"] = df["Name"].str.strip().str.title()

# ----------------------------------------
# Practice: Load and Clean Practice File
# ----------------------------------------

df = pd.read_csv("messy_practice.csv")
print(df.isnull().sum())

df["Score"].replace("not_available", pd.NA, inplace=True)
print(df["Score"])

df["Score"] = pd.to_numeric(df["Score"], errors="coerce")
print(df.dtypes)

# Remove duplicate rows
before = len(df)
df.drop_duplicates(inplace=True)
after = len(df)
print("Duplicates removed:", before - after)

# Clean Name column
df["Name"] = df["Name"].str.strip().str.title()
print(df["Name"])

# ----------------------------------------
# Save the Cleaned Data to File
# ----------------------------------------

df.to_csv("cleaned_scores.csv", index=False)

