# ----------------------------------------
# Create Sample Data
# ----------------------------------------

import matplotlib.pyplot as plt

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
scores = [85, 78, 92, 88, 76]
weeks = [1, 2, 3, 4]
visits = [150, 200, 250, 300]
heights = [160, 175, 168, 180, 170]
weights = [55, 75, 65, 85, 60]

# ----------------------------------------
# Line Plot: Website Visits Over Time
# ----------------------------------------

plt.plot(weeks, visits)
plt.title("Website Visits Over Time")
plt.xlabel("Week")
plt.ylabel("Number of Visits")
plt.grid(True)
plt.show()

# ----------------------------------------
# Bar Chart: Student Test Scores
# ----------------------------------------

plt.bar(names, scores)
plt.title("Student Test Scores")
plt.xlabel("Name")
plt.ylabel("Score")
plt.show()

# ----------------------------------------
# Histogram: Score Distribution
# ----------------------------------------

plt.hist(scores, bins=5, edgecolor="black")
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.show()

# ----------------------------------------
# Box Plot: Summary of Scores
# ----------------------------------------

plt.boxplot(scores)
plt.title("Box Plot of Scores")
plt.ylabel("Score")
plt.grid(True)
plt.show()

# ----------------------------------------
# Scatter Plot: Height vs Weight
# ----------------------------------------

plt.scatter(heights, weights)
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.show()

# ----------------------------------------
# Create CSV File with Scores
# ----------------------------------------

with open("scores.csv", "w") as file:
    file.write("Name,Score\n")
    file.write("Alice,85\n")
    file.write("Bob,90\n")
    file.write("Charlie,78\n")
    file.write("Daisy,65\n")
    file.write("Ethan,55\n")
    file.write("Fiona,92\n")
    file.write("George,80\n")

# ----------------------------------------
# Read CSV Using Pandas
# ----------------------------------------

import pandas as pd

df = pd.read_csv("scores.csv")
print(df)

# ----------------------------------------
# Visualize CSV Data with Matplotlib
# ----------------------------------------

plt.figure()
plt.bar(df["Name"], df["Score"])
plt.title("Student Scores from CSV")
plt.xlabel("Student Name")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
plt.boxplot(df["Score"])
plt.title("Score Distribution (CSV)")
plt.ylabel("Score")
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------------------
# Quick Bar Plot with Pandas
# ----------------------------------------

df.plot(kind="bar", x="Name", y="Score")
plt.title("Scores by Name")
plt.xlabel("Student Name")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------------------
# Seaborn: Box Plot of Scores
# ----------------------------------------

import seaborn as sns

df = pd.read_csv("scores.csv")
sns.boxplot(y="Score", data=df)
plt.title("Score Distribution (from CSV)")
plt.ylabel("Score")
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------------------
# Seaborn: Histogram with KDE
# ----------------------------------------

sns.histplot(data=df, x="Score", bins=5, kde=True)
plt.title("Distribution of Scores")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# ----------------------------------------
# Seaborn: Scatter Plot of Height vs Weight
# ----------------------------------------

df = pd.DataFrame({
    "Height": [160, 165, 170, 175, 180],
    "Weight": [50, 60, 65, 75, 85]
})
sns.scatterplot(x="Height", y="Weight", data=df)
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------------------
# Seaborn: Average Score per Class
# ----------------------------------------

df = pd.DataFrame({
    "Class": ["A", "A", "B", "B", "C", "C"],
    "Score": [85, 90, 75, 78, 92, 88]
})
sns.barplot(x="Class", y="Score", data=df)
plt.title("Average Score per Class")
plt.xlabel("Class")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()

# ----------------------------------------
# Seaborn: Correlation Heatmap
# ----------------------------------------

df = pd.DataFrame({
    "Math": [85, 90, 78, 92, 88],
    "Science": [80, 89, 75, 95, 85],
    "English": [78, 85, 74, 88, 82]
})
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="Blues")
plt.title("Correlation Between Subjects")
plt.tight_layout()
plt.show()

# ----------------------------------------
# Seaborn: Violin Plot by Class
# ----------------------------------------

df = pd.DataFrame({
    "Class": ["A", "A", "B", "B", "C", "C"],
    "Score": [85, 90, 75, 78, 92, 88]
})
sns.violinplot(x="Class", y="Score", data=df)
plt.title("Score Distribution by Class")
plt.xlabel("Class")
plt.ylabel("Score")
plt.tight_layout()
plt.show()

# ----------------------------------------
# Seaborn: Pair Plot for Subjects
# ----------------------------------------

df = pd.DataFrame({
    "Math": [85, 90, 78, 92, 88],
    "Science": [80, 89, 75, 95, 85],
    "English": [78, 85, 74, 88, 82]
})
sns.pairplot(df)
plt.suptitle("Pairwise Relationships Between Subjects", y=1.02)
plt.tight_layout()
plt.show()
