# ----------------------------------------
# Import Libraries
# ----------------------------------------

import pandas as pd                      # Used for data manipulation
import matplotlib.pyplot as plt          # Used for data visualization
import seaborn as sns                    # Used for advanced visualizations

# ----------------------------------------
# Create Dataset
# ----------------------------------------

scores = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Score": [85, 78, 92, 88, 76],
    "Height": [160, 175, 168, 180, 170],
    "Weight": [55, 75, 65, 85, 60]
})

# ----------------------------------------
# Basic Statistics
# ----------------------------------------

mean_score = scores["Score"].mean()         # Calculate average score
median_height = scores["Height"].median()   # Find the middle value of height
std_score = scores["Score"].std()           # Calculate standard deviation of score
correlation = scores[["Height", "Weight"]].corr()  # Calculate correlation matrix

# Display results
print("Mean Score:", mean_score)
print("Median Height:", median_height)
print("Score Standard Deviation:", std_score)
print("Correlation (Height vs Weight):")
print(correlation)

# ----------------------------------------
# Visualize Statistics with Subplots
# ----------------------------------------

fig, axs = plt.subplots(4, 1, figsize=(8, 10), constrained_layout=True)

# Bar chart with mean line
axs[0].bar(scores["Name"], scores["Score"], color='skyblue')
axs[0].axhline(mean_score, color='blue', linestyle='--', label=f"Mean: {mean_score:.1f}")
axs[0].set_title("Mean Score")
axs[0].legend()

# Median plot
axs[1].plot(sorted(scores["Height"]), marker='o', color='black')
axs[1].scatter(2, median_height, color='red', label=f"Median: {median_height}")
axs[1].set_title("Median Height")
axs[1].legend()

# Histogram for scores
sns.histplot(scores["Score"], bins=5, ax=axs[2], kde=True, color='lightgreen')
axs[2].axvline(mean_score, color='blue', linestyle='--', label="Mean")
axs[2].axvline(mean_score + std_score, color='gray', linestyle=':', label="+1 SD")
axs[2].axvline(mean_score - std_score, color='gray', linestyle=':', label="-1 SD")
axs[2].set_title("Score Distribution and Standard Deviation")
axs[2].legend()

# Scatterplot for correlation
sns.regplot(x="Height", y="Weight", data=scores, ax=axs[3], color='green')
axs[3].set_title("Correlation Between Height and Weight")

# Save and show plot
plt.savefig("statistics_visual_analogy_generated.png", dpi=300)
plt.show()


# ----------------------------------------
# Create exam_summary.csv Dataset
# ----------------------------------------

import pandas as pd  # Import pandas for data handling

# Define the exact dataset used in the chapter
exam_data = pd.DataFrame({
    "Name": ["Jake", "Lily", "Omar", "Nina", "Ravi", "Sara", "Leo", "Tina"],
    "Score": [67, 74, 91, 85, 80, 60, 88, 70],
    "Height": [162, 170, 168, 180, 158, 165, 172, 169],
    "Weight": [54, 70, 60, 82, 50, 65, 68, 64]
})

# Save to CSV file
exam_data.to_csv("exam_summary.csv", index=False)

# Confirmation
print("exam_summary.csv has been created successfully.")

# ----------------------------------------
# Load Dataset from CSV
# ----------------------------------------

df = pd.read_csv("exam_summary.csv")   # Load the CSV file

# ----------------------------------------
# Practice: Calculate Statistics
# ----------------------------------------

print("Mean Score:", df["Score"].mean())         # Mean score
print("Median Height:", df["Height"].median())   # Median height
print("Score Standard Deviation:", df["Score"].std())  # Score SD
print(df[["Height", "Weight"]].corr())           # Correlation matrix

# ----------------------------------------
# Optional: Manual Mean and SD Calculation
# ----------------------------------------

scores_list = [67, 74, 91, 85, 80]

total = sum(scores_list)
n = len(scores_list)
mean = total / n
print("Manual Mean:", mean)

squared_diffs = [(x - mean)**2 for x in scores_list]
variance = sum(squared_diffs) / (n - 1)
std_dev = variance**0.5
print("Manual Standard Deviation:", std_dev)

# ----------------------------------------
# Challenge: BMI Calculation
# ----------------------------------------

df["Height_m"] = df["Height"] / 100                      # Convert cm to meters
df["BMI"] = df["Weight"] / (df["Height_m"] ** 2)         # Calculate BMI
print("Mean BMI:", round(df["BMI"].mean(), 2))           # Mean BMI
print("Standard Deviation of BMI:", round(df["BMI"].std(), 2))  # SD of BMI

# ----------------------------------------
# Challenge: Score Deviation Analysis
# ----------------------------------------

mean_score = df["Score"].mean()
df["ScoreDeviation"] = abs(df["Score"] - mean_score)     # Absolute deviation
outlier = df.loc[df["ScoreDeviation"].idxmax()]          # Student with max deviation
print("Student with biggest score deviation:")
print(outlier[["Name", "Score", "ScoreDeviation"]])

