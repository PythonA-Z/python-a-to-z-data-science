# ---------------------------------------- 
# Importing Pandas and Creating DataFrame
# ----------------------------------------

import pandas as pd  # Import the pandas library

# Create a simple table (DataFrame) using a Python dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [85, 90, 78]
}

# Convert dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# ----------------------------------------
# Reading and Saving CSV Files
# ----------------------------------------

# Read data from an existing CSV file
df = pd.read_csv("scores.csv")  # Make sure 'scores.csv' exists in the same folder
print(df)

# Save the DataFrame to a new CSV file
df.to_csv("output.csv", index=False)  # 'index=False' avoids writing row numbers

# ----------------------------------------
# Exploring the Data
# ----------------------------------------

print(df.head())       # First 5 rows
print(df.tail())       # Last 5 rows
print(df.info())       # Column types and non-null counts
print(df.describe())   # Statistics for numeric columns
print(df.columns)      # List of column names
print(df.shape)        # (rows, columns)

# ----------------------------------------
# Selecting Data
# ----------------------------------------

print(df["Score"])               # Select one column (as a Series)
print(df[["Name", "Score"]])     # Select multiple columns (as a new DataFrame)
print(df.loc[1])                 # Select row by index label
print(df[df["Score"] > 80])      # Filter rows where Score > 80

# ----------------------------------------
# Practice Question 1: View first few rows
# ----------------------------------------

df = pd.read_csv("scores.csv")  # Reload the data
print(df.head())                # Show first 5 rows

# ----------------------------------------
# Practice Question 2: Select Score column
# ----------------------------------------

print(df["Score"])  # Only the "Score" column

# ----------------------------------------
# Practice Question 3: Filter Scores > 80
# ----------------------------------------

print(df[df["Score"] > 80])  # Show rows where Score > 80

# ----------------------------------------
# Practice Question 4: Add "Result" Column
# ----------------------------------------

# Add a new column showing "Pass" or "Fail" based on score
df["Result"] = df["Score"].apply(lambda x: "Pass" if x >= 60 else "Fail")
print(df)

# ----------------------------------------
# Practice Question 5: Save Updated File
# ----------------------------------------

# Save the updated DataFrame to a new CSV
df.to_csv("graded_scores.csv", index=False)

# ----------------------------------------
# Bonus: Add Grade Column (A/B/C)
# ----------------------------------------

# Define grading rules
def grade_label(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

# Apply grade function to each row
df["Grade"] = df["Score"].apply(grade_label)
print(df)

# ----------------------------------------
# Interview Challenge Solutions
# ----------------------------------------

df = pd.read_csv("scores.csv")  # Reload clean data

print(df.head(3))  # First 3 rows only
print(df["Name"])  # Only the Name column
print(df[df["Score"] < 80])  # Students who scored less than 80

# Add a "Passed" column based on Score >= 60
df["Passed"] = df["Score"].apply(lambda x: "Yes" if x >= 60 else "No")
print(df)

# Save result to a new file
df.to_csv("pass_results.csv", index=False)

# ----------------------------------------
# Mini Project: Analyze Scores
# ----------------------------------------

df = pd.read_csv("scores.csv")  # Load the file again

# Step 1: Filter students with scores above 80
above_80 = df[df["Score"] > 80]
print("Scores above 80:")
print(above_80)

# Step 2: Calculate the average score
avg = df["Score"].mean()
print("\nAverage Score:", avg)

# Step 3: Assign letter grades
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

# Apply the function to add a new Grade column
df["Grade"] = df["Score"].apply(get_grade)
print("\nFinal DataFrame with Grades:")
print(df)
