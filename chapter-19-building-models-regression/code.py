# ----------------------------------------
# Import Libraries and Load Raw Dataset
# ----------------------------------------

import pandas as pd

# Load the raw dataset
data = pd.read_csv("ames_unclean.csv")  # Load data from a CSV file into a DataFrame

# Preview the first few rows
print(data.head())

# Check for missing values
print(data.isnull().sum())

# ----------------------------------------
# Drop Missing Values and Save Cleaned Version
# ----------------------------------------
# Drop rows with any missing values
data_cleaned = data.dropna()  # Remove rows with missing values

# Save the cleaned version
data_cleaned.to_csv("ames_clean.csv", index=False)  # Save the DataFrame to a CSV file

# Check for missing values in cleaned version 
print(data_cleaned.isnull().sum())

# ----------------------------------------
# Encode Categorical Variables and Save Encoded File
# ----------------------------------------

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder  # Import tool to encode ordered categories as numbers

# 1. Load the cleaned housing dataset
data = pd.read_csv('ames_clean.csv')  # Load data from a CSV file into a DataFrame

# 2. Convert ranked qualities to numbers (Ordinal Encoding)
ordinal_map = {
    'Kitchen Qual': ['Po','Fa', 'TA', 'Gd', 'Ex'],
    'Bsmt Qual': ['Po','Fa', 'TA', 'Gd', 'Ex']
}
ordinal_encoder = OrdinalEncoder(categories=[ordinal_map[col] for col in ordinal_map])  # Import tool to encode ordered categories as numbers
data[list(ordinal_map)] = ordinal_encoder.fit_transform(data[list(ordinal_map)])

# 3. Convert Yes/No to 1/0 (Binary Encoding)
data['Central Air'] = data['Central Air'].map({'Y': 1, 'N': 0})  # Convert Yes/No to 1/0 for binary encoding

# 4. Convert unordered categories to dummy columns (One-Hot Encoding)
one_hot_columns = ['Neighborhood', 'Garage Type', 'MS Zoning', 'House Style']
data_encoded = pd.get_dummies(data, columns=one_hot_columns, drop_first=True)  # Perform one-hot encoding on categorical columns

# 5. Save the fully encoded version for future use
data_encoded.to_csv('ames_encoded.csv', index=False)  # Save the DataFrame to a CSV file

# 6. See which features are most related to SalePrice
corr_with_price = data_encoded.corr()['SalePrice'].sort_values(ascending=False).drop('SalePrice')

# 7. Plot the top correlations with SalePrice
plt.figure(figsize=(10, 12))
sns.barplot(x=corr_with_price.values, y=corr_with_price.index)
plt.title('How Strongly Each Feature Is Related to SalePrice')
plt.tight_layout()
plt.savefig('correlation_with_saleprice_encoded.png')
plt.show()  # Display the generated plot

# ----------------------------------------
# Visualize Feature Correlation with SalePrice
# ----------------------------------------

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

# Load the encoded dataset
data_encoded = pd.read_csv('ames_encoded.csv')  # Load data from a CSV file into a DataFrame

# Correlation of all features with SalePrice
corr_with_saleprice = data_encoded.corr(numeric_only=True)[['SalePrice']].drop('SalePrice')

# Plot heatmap
plt.figure(figsize=(8, len(corr_with_saleprice) * 0.4))
sns.heatmap(
    corr_with_saleprice,
    annot=True,
    fmt=".2f",
    cmap='coolwarm',
    linewidths=0.5,
    linecolor='black',
    cbar=True,
    square=False
)
plt.title('Correlation of SalePrice with Other Features', fontsize=14, pad=20)
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('saleprice_correlation_heatmap.png', dpi=300)
plt.show()  # Display the generated plot

# ----------------------------------------
# Heatmap: Correlation with SalePrice
# ----------------------------------------

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

# Load the encoded dataset
data_encoded = pd.read_csv('ames_encoded.csv')  # Load data from a CSV file into a DataFrame

# Find the top 5 features most correlated with SalePrice
correlations = data_encoded.corr(numeric_only=True)['SalePrice'].drop('SalePrice')
top5 = correlations.sort_values(ascending=False).head(5)

# Plot top 5 correlated features
plt.figure(figsize=(8, 5))
sns.barplot(x=top5.values, y=top5.index, palette="Blues_d")
plt.title("Top 5 Features Most Correlated with SalePrice")
plt.xlabel("Correlation")
plt.tight_layout()
plt.show()  # Display the generated plot

# ----------------------------------------
# Bar Plot: Top 5 Most Correlated Features
# ----------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split  # Split data into training and testing sets
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score  # Measures average error between actual and predicted values  # Measures how well the model explains price variation

# Load the encoded dataset
data_encoded = pd.read_csv('ames_encoded.csv')  # Load data from a CSV file into a DataFrame

# Separate features and target
X = data_encoded.drop('SalePrice', axis=1)
y = data_encoded['SalePrice']

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # Split data into training and testing sets

# Create and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)  # Train the model on training data

# Predict house prices on the test set
y_pred = model.predict(X_test)  # Use the trained model to make predictions

# Evaluate the models accuracy
mae = mean_absolute_error(y_test, y_pred)  # Measures average error between actual and predicted values
r2 = r2_score(y_test, y_pred)  # Measures how well the model explains price variation

print(f"Mean Absolute Error: {mae:.0f}")
print(f"R^2 Score: {r2:.2f}")

# ----------------------------------------
# Random Forest Regression Model
# ----------------------------------------

import matplotlib.pyplot as plt

import seaborn as sns

# Scatter plot of actual vs predicted sale prices
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Actual SalePrice")
plt.ylabel("Predicted SalePrice")
plt.title("Actual vs. Predicted House Prices (Random Forest)")
plt.tight_layout()
plt.savefig("actual_vs_predicted_prices_rf.png")
plt.show()  # Display the generated plot

# ----------------------------------------
# Plot: Actual vs Predicted Prices (Random Forest)
# ----------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split  # Split data into training and testing sets
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score  # Measures average error between actual and predicted values  # Measures how well the model explains price variation

data = pd.read_csv("ames_encoded.csv")  # Load data from a CSV file into a DataFrame
X = data.drop("SalePrice", axis=1)
y = data["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # Split data into training and testing sets

gb_model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
gb_model.fit(X_train, y_train)  # Train the model on training data

y_pred = gb_model.predict(X_test)  # Use the trained model to make predictions

mae = mean_absolute_error(y_test, y_pred)  # Measures average error between actual and predicted values
r2 = r2_score(y_test, y_pred)  # Measures how well the model explains price variation

print("Mean Absolute Error:", round(mae))
print("R^2 Score:", round(r2, 2))

# ----------------------------------------
# Gradient Boosting Regressor Model
# ----------------------------------------

import pandas as pd

import numpy as np
from sklearn.model_selection import train_test_split  # Split data into training and testing sets
from sklearn.metrics import mean_absolute_error, r2_score  # Measures average error between actual and predicted values  # Measures how well the model explains price variation
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

import matplotlib.pyplot as plt

data = pd.read_csv("ames_encoded.csv")  # Load data from a CSV file into a DataFrame
X = data.drop("SalePrice", axis=1)
y = data["SalePrice"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Split data into training and testing sets

# Model comparisons
models = {
    "Linear": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42),
    "Ridge (log)": Ridge()
}

mae_scores = []
r2_scores = []  # Measures how well the model explains price variation

# Linear, RF, GB
for name, model in list(models.items())[:3]:
    model.fit(X_train, y_train)  # Train the model on training data
    y_pred = model.predict(X_test)  # Use the trained model to make predictions
    mae_scores.append(mean_absolute_error(y_test, y_pred))  # Measures average error between actual and predicted values
    r2_scores.append(r2_score(y_test, y_pred))  # Measures how well the model explains price variation

# Ridge with log transformation
y_log = np.log(y)
X_train_log, X_test_log, y_train_log, y_test_log = train_test_split(X, y_log, test_size=0.2, random_state=42)  # Split data into training and testing sets
ridge_model = models["Ridge (log)"]
ridge_model.fit(X_train_log, y_train_log)  # Train the model on training data
pred_log = ridge_model.predict(X_test_log)  # Use the trained model to make predictions
y_pred_ridge = np.exp(pred_log)
mae_scores.append(mean_absolute_error(y_test, y_pred_ridge))  # Measures average error between actual and predicted values
r2_scores.append(r2_score(y_test, y_pred_ridge))  # Measures how well the model explains price variation

# MAE plot
plt.figure(figsize=(8, 4))
plt.bar(models.keys(), mae_scores, color='skyblue')
plt.ylabel("Mean Absolute Error ($)")
plt.title("Model Comparison: MAE")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("model_comparison_mae.png")
plt.show()  # Display the generated plot

# R^2 plot
plt.figure(figsize=(8, 4))
plt.bar(models.keys(), r2_scores, color='lightgreen')  # Measures how well the model explains price variation
plt.ylabel("R Square Score")
plt.title("Model Comparison: R Square Score")
plt.xticks(rotation=15)
plt.ylim(0.80, 0.95)
plt.tight_layout()
plt.savefig("model_comparison_r2.png")
plt.show()  # Display the generated plot

# ----------------------------------------
# Model Comparison: Linear, RF, GB, Ridge (Log)
# ----------------------------------------
plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred, alpha=0.5, color="steelblue")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Actual SalePrice ($)")
plt.ylabel("Predicted SalePrice ($)")
plt.title("Gradient Boosting: Actual vs Predicted Prices")
plt.tight_layout()
plt.savefig("actual_vs_predicted_gradient.png")
plt.show()  # Display the generated plot
