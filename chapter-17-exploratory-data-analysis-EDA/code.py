# ----------------------------------------
# Exploratory Data Analysis (EDA) Project
# ----------------------------------------

# Step 1: Import Required Libraries
import pandas as pd  # For data loading and DataFrame operations
import seaborn as sns  # For advanced and beautiful visualizations
import matplotlib.pyplot as plt  # For basic plotting
import numpy as np  # For numeric operations like average, array math
import squarify  # For drawing treemaps (space-filling visuals)
import missingno as msno  # For visualizing missing values in the dataset

# ----------------------------------------
# Step 2: Load and Prepare the Dataset
# ----------------------------------------

# Load data from CSV
data = pd.read_csv("customer_purchase.csv")  # Load data from a CSV file into a DataFrame

# Convert 'PurchaseDate' column to datetime
data['PurchaseDate'] = pd.to_datetime(data['PurchaseDate'])  # Convert column to datetime format (for time plots)

# ----------------------------------------
# Step 3: Explore Data Types and Summary
# ----------------------------------------

print(data.dtypes)  # Check column types  # Shows the data type of each column
print(data.info())  # Data overview  # Gives non-null counts and memory usage
print(data.describe())  # Statistical summary  # Summary stats: mean, min, max, etc.

# ----------------------------------------
# Step 4: Univariate Analysis (One Column)
# ----------------------------------------

# Histogram of customer age
sns.histplot(data['Age'], bins=8, kde=True)  # Draws a histogram (distribution of values)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Boxplot of PurchaseAmount
sns.boxplot(x=data['PurchaseAmount'])  # Boxplot helps find outliers in the data
plt.title("Distribution of Purchase Amounts")
plt.xlabel("Purchase Amount")
plt.show()

# ----------------------------------------
# Step 5: Categorical Counts
# ----------------------------------------

# Countplot for Gender
sns.countplot(x='Gender', data=data)  # Bar chart showing count of each category
plt.title("Gender Distribution")
plt.show()

# Countplot for ProductCategory
sns.countplot(x='ProductCategory', data=data)  # Bar chart showing count of each category
plt.title("Products Purchased")
plt.xticks(rotation=45)
plt.show()

# ----------------------------------------
# Step 6: Bivariate Analysis
# ----------------------------------------

# Scatter plot: Age vs PurchaseAmount
sns.scatterplot(x='Age', y='PurchaseAmount', data=data)  # Plot relationship between two numeric columns
plt.title("Age vs Purchase Amount")
plt.show()
print(data[['Age', 'PurchaseAmount']].corr())  # Calculate correlation between numeric columns

# Boxplot: Gender vs PurchaseAmount
sns.boxplot(x='Gender', y='PurchaseAmount', data=data)  # Boxplot helps find outliers in the data
plt.title("Purchase Amount by Gender")
plt.show()

# Barplot: Average Spend by Product Category
sns.barplot(x='ProductCategory', y='PurchaseAmount', data=data, estimator=np.mean)  # Shows average values by category (with error bars)
plt.title("Average Spend by Product Category")
plt.xticks(rotation=45)
plt.show()

# ----------------------------------------
# Step 7: Time Series Plot
# ----------------------------------------

daily_sales = data.groupby('PurchaseDate')['PurchaseAmount'].sum().reset_index()
sns.lineplot(x='PurchaseDate', y='PurchaseAmount', data=daily_sales)
plt.title('Daily Purchase Amount Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------------------
# Step 8: Missing Values & Duplicates
# ----------------------------------------

print(data.isnull().sum())  # Check missing values
msno.matrix(data)  # Visualize missingness  # Show where missing data exists
plt.show()

# Handle missing values
data['Age'].fillna(data['Age'].mean(), inplace=True)  # Fill missing values with mean or mode
data['City'].fillna(data['City'].mode()[0], inplace=True)  # Fill missing values with mean or mode

# Drop duplicates
data = data.drop_duplicates()  # Remove repeated rows from the data

# ----------------------------------------
# Step 9: Advanced Visualizations
# ----------------------------------------

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data[['Age', 'PurchaseAmount']].corr(), annot=True, cmap='coolwarm')  # Calculate correlation between numeric columns
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# Violin Plot
sns.violinplot(x='ProductCategory', y='PurchaseAmount', data=data)
plt.title("Violin Plot by Product Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Swarm Plot
sns.swarmplot(x='ProductCategory', y='PurchaseAmount', data=data)
plt.title("Swarm Plot of Purchases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Boxen Plot
sns.boxenplot(x='ProductCategory', y='PurchaseAmount', data=data)
plt.title("Boxen Plot of Purchases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Facet Grid by Gender
g = sns.FacetGrid(data, col="Gender", height=5, aspect=1)  # Creates separate plots for each group (like Gender)
g.map_dataframe(sns.histplot, x="PurchaseAmount", bins=10)  # Draws a histogram (distribution of values)
g.fig.suptitle("Purchase Distribution by Gender", y=1.05)
plt.tight_layout()
plt.show()

# Treemap
category_sales = data.groupby('ProductCategory')['PurchaseAmount'].sum().reset_index()
plt.figure(figsize=(10, 6))
squarify.plot(sizes=category_sales['PurchaseAmount'],  # Draw the treemap showing total spend per category
              label=category_sales['ProductCategory'], alpha=0.8)
plt.title("Treemap of Purchases")
plt.axis("off")
plt.tight_layout()
plt.show()

# Radar Chart
categories = list(data['ProductCategory'].unique())
values = data.groupby('ProductCategory')['PurchaseAmount'].mean().reindex(categories).values  # Group by category and calculate average spend
N = len(categories)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
values = np.append(values, values[0])
angles += angles[:1]
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
plt.xticks(angles[:-1], categories)
ax.set_rlabel_position(0)
plt.yticks([50, 100, 150, 200], ["50", "100", "150", "200"], color="grey", size=7)
plt.ylim(0, max(values))
ax.plot(angles, values, linewidth=1, linestyle='solid')  # Radar chart to compare multiple category averages
ax.fill(angles, values, 'b', alpha=0.1)
plt.title("Radar Chart: Avg Spend by Category", y=1.1)
plt.tight_layout()
plt.show()

# ----------------------------------------
# Step 10: Dashboard Summary & Reporting
# ----------------------------------------

# 2x2 Dashboard Layout
fig, axs = plt.subplots(2, 2, figsize=(12, 10))  # Create a dashboard layout with multiple plots
sns.histplot(data=data, x='Age', kde=True, ax=axs[0, 0])  # Draws a histogram (distribution of values)
axs[0, 0].set_title('Age Distribution')
sns.histplot(data=data, x='PurchaseAmount', kde=True, ax=axs[0, 1])  # Draws a histogram (distribution of values)
axs[0, 1].set_title('Purchase Amount Distribution')
top5 = data['ProductCategory'].value_counts().nlargest(5).reset_index()
top5.columns = ['ProductCategory', 'Count']
sns.barplot(data=top5, x='ProductCategory', y='Count', ax=axs[1, 0])  # Shows average values by category (with error bars)
axs[1, 0].set_title('Top 5 Product Categories')
avg_by_gender = data.groupby('Gender')['PurchaseAmount'].mean().reset_index()  # Group by category and calculate average spend
sns.barplot(data=avg_by_gender, x='Gender', y='PurchaseAmount', ax=axs[1, 1])  # Shows average values by category (with error bars)
axs[1, 1].set_title('Avg Spend by Gender')
plt.tight_layout()
plt.show()

# Boxplot to detect outliers
sns.boxplot(data=data, x='ProductCategory', y='PurchaseAmount')  # Boxplot helps find outliers in the data
plt.title('Outliers by Product Category')
plt.tight_layout()
plt.show()

# Top Spending Groups
grouped = data.groupby(['Gender', 'ProductCategory'])['PurchaseAmount'].mean()  # Group by category and calculate average spend
top_groups = grouped.sort_values(ascending=False).head(5).round(0)  # Sort results from highest to lowest
print("Top Spending Groups:
", top_groups)

