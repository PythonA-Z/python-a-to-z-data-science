# ----------------------------------------
# Importing Pandas and Creating DataFrame
# ----------------------------------------

import pandas as pd

# Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [85, 90, 78]
}
df = pd.DataFrame(data)
print(df)

# ----------------------------------------
# Reading and Saving CSV Files
# ----------------------------------------

df = pd.read_csv("scores.csv")  # Make sure scores.csv exists
print(df)

df.to_csv("output.csv", index=False)

# ----------------------------------------
# Exploring the Data
# ----------------------------------------

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape)

# ----------------------------------------
# Selecting Data
# ----------------------------------------

print(df["Score"])
print(df[["Name", "Score"]])
print(df.loc[1])
print(df[df["Score"] > 80])

# ----------------------------------------
# Practice Question 1
# ----------------------------------------

df = pd.read_csv("scores.csv")
print(df.head())

# ----------------------------------------
# Practice Question 2
# ----------------------------------------

print(df["Score"])

# ----------------------------------------
# Practice Question 3
# ----------------------------------------

print(df[df["Score"] > 80])

# ----------------------------------------
# Practice Question 4: Add "Result" Column
# ----------------------------------------

df["Result"] = df["Score"].apply(lambda x: "Pass" if x >= 60 else "Fail")
print(df)

# ----------------------------------------
# Practice Question 5: Save Updated File
# ----------------------------------------

df.to_csv("graded_scores.csv", index=False)

# ----------------------------------------
# Bonus: Add Grade Column
# ----------------------------------------

def grade_label(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

df["Grade"] = df["Score"].apply(grade_label)
print(df)

# ----------------------------------------
# Interview Challenge Solutions
# ----------------------------------------

print(df.head(3))
print(df["Name"])
print(df[df["Score"] < 80])
df["Passed"] = df["Score"].apply(lambda x: "Yes" if x >= 60 else "No")
print(df)
df.to_csv("pass_results.csv", index=False)

# ----------------------------------------
# Mini Project: Analyze Scores
# ----------------------------------------

df = pd.read_csv("scores.csv")

above_80 = df[df["Score"] > 80]
print("Scores above 80:")
print(above_80)

avg = df["Score"].mean()
print("\nAverage Score:", avg)

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

df["Grade"] = df["Score"].apply(get_grade)
print("\nFinal DataFrame with Grades:")
print(df)

