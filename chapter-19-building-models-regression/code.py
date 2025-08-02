
# ----------------------------------------
# Load Raw Dataset and Check Missing Values

# ----------------------------------------
import pandas as pd

# Load the raw dataset
data = pd.read_csv("ames_unclean.csv")  # Load data from a CSV file into a DataFrame

# Preview the first few rows
print(data.head())

# Check for missing values
print(data.isnull().sum())


# ----------------------------------------
# Drop Missing Values and Save Cleaned Data

# ----------------------------------------
# Drop rows with any missing values
data_cleaned = data.dropna()  # Remove rows with any missing values

# Save the cleaned version
data_cleaned.to_csv("ames_clean.csv", index=False)  # Save the DataFrame to a new CSV file

# Check for missing values in cleaned version 
print(data_cleaned.isnull().sum())


# ----------------------------------------
# Encode Categorical Features (Ordinal, Binary, One-Hot)

# ----------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder  # Used to convert ordered categories (e.g., quality levels) into numbers

# 1. Load the cleaned housing dataset
data = pd.read_csv('ames_clean.csv')  # Load data from a CSV file into a DataFrame

# 2. Convert ranked qualities to numbers (Ordinal Encoding)
ordinal_map = {
    'Kitchen Qual': ['Po','Fa', 'TA', 'Gd', 'Ex'],
    'Bsmt Qual': ['Po','Fa', 'TA', 'Gd', 'Ex']
}
ordinal_encoder = OrdinalEncoder(categories=[ordinal_map[col] for col in ordinal_map])  # Used to convert ordered categories (e.g., quality levels) into numbers
data[list(ordinal_map)] = ordinal_encoder.fit_transform(data[list(ordinal_map)])

# 3. Convert Yes/No to 1/0 (Binary Encoding)
data['Central Air'] = data['Central Air'].map({'Y': 1, 'N': 0})  # Convert Yes/No to 1 and 0

# 4. Convert unordered categories to dummy columns (One-Hot Encoding)
one_hot_columns = ['Neighborhood', 'Garage Type', 'MS Zoning', 'House Style']
data_encoded = pd.get_dummies(data, columns=one_hot_columns, drop_first=True)  # One-hot encode categorical columns (convert text labels to 0/1 columns)

# 5. Save the fully encoded version for future use
data_encoded.to_csv('ames_encoded.csv', index=False)  # Save the DataFrame to a new CSV file

# 6. See which features are most related to SalePrice
corr_with_price = data_encoded.corr()['SalePrice'].sort_values(ascending=False).drop('SalePrice')  # Calculate how strongly each feature is correlated with SalePrice

# 7. Plot the top correlations with SalePrice
plt.figure(figsize=(10, 12))
sns.barplot(x=corr_with_price.values, y=corr_with_price.index)
plt.title('How Strongly Each Feature Is Related to SalePrice')
plt.tight_layout()
plt.savefig('correlation_with_saleprice_encoded.png')
plt.show()  # Display the plot


# ----------------------------------------
# Save Encoded Dataset and Plot Feature Correlation

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
plt.show()  # Display the plot


# ----------------------------------------
# Plot Top 5 Most Correlated Features

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
plt.show()  # Display the plot


# ----------------------------------------
# Train a Random Forest Regression Model

# ----------------------------------------
import pandas as pd
from sklearn.model_selection import train_test_split  # Split dataset into training and testing sets
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score  # Measure average prediction error

# Load the encoded dataset
data_encoded = pd.read_csv('ames_encoded.csv')  # Load data from a CSV file into a DataFrame

# Separate features and target
X = data_encoded.drop('SalePrice', axis=1)
y = data_encoded['SalePrice']

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # Split dataset into training and testing sets

# Create and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)  # Train the model on training data

# Predict house prices on the test set
y_pred = model.predict(X_test)  # Use the model to predict target values

# Evaluate the models accuracy
mae = mean_absolute_error(y_test, y_pred)  # Measure average prediction error
r2 = r2_score(y_test, y_pred)  # Measure how well the model explains variation in the target

print(f"Mean Absolute Error: {mae:.0f}")
print(f"R^2 Score: {r2:.2f}")


# ----------------------------------------
# Plot Actual vs Predicted Prices (Random Forest)

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
plt.show()  # Display the plot


# ----------------------------------------
# Train a Gradient Boosting Regressor

# ----------------------------------------
import pandas as pd
from sklearn.model_selection import train_test_split  # Split dataset into training and testing sets
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score  # Measure average prediction error

data = pd.read_csv("ames_encoded.csv")  # Load data from a CSV file into a DataFrame
X = data.drop("SalePrice", axis=1)
y = data["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # Split dataset into training and testing sets

gb_model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
gb_model.fit(X_train, y_train)  # Train the model on training data

y_pred = gb_model.predict(X_test)  # Use the model to predict target values

mae = mean_absolute_error(y_test, y_pred)  # Measure average prediction error
r2 = r2_score(y_test, y_pred)  # Measure how well the model explains variation in the target

print("Mean Absolute Error:", round(mae))
print("R^2 Score:", round(r2, 2))



# ----------------------------------------
# Mini Coding Challenge Solutions

# ----------------------------------------


 # Step 1: Regular Linear Regression
 
	from sklearn.linear_model import LinearRegression
	from sklearn.model_selection import train_test_split
	from sklearn.metrics import mean_absolute_error, r2_score
	import pandas as pd
	
	# Load encoded data
	data = pd.read_csv("ames_encoded.csv")
	
	# Select features and target
	X = data[['Gr Liv Area', 'Overall Qual', 'Year Built']]
	y = data['SalePrice']
	
	# Train-test split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
	
	# Train linear regression model
	model = LinearRegression()
	model.fit(X_train, y_train)
	
	# Predict and evaluate
	y_pred = model.predict(X_test)
	mae = mean_absolute_error(y_test, y_pred)
	r2 = r2_score(y_test, y_pred)
	print("MAE:", mae)
	print("R^2:", r2)


 # Step 2: Linear Regression with Log-Transformed Target

    import numpy as np
	
	# Log transform the target
	y_log = np.log(y)
	
	# Train-test split
	X_train_log, X_test_log, y_train_log, y_test_log = train_test_split(
	X, y_log, test_size=0.3, random_state=42)
	
	# Train model
	model_log = LinearRegression()
	model_log.fit(X_train_log, y_train_log)
	
	# Predict and convert back to original scale
	y_pred_log = model_log.predict(X_test_log)
	y_pred_original = np.exp(y_pred_log)
	y_actual_original = np.exp(y_test_log)
	
	# Evaluate
	mae_log = mean_absolute_error(y_actual_original, y_pred_original)
	r2_log = r2_score(y_actual_original, y_pred_original)
	print("MAE (log):", mae_log)
	print("R^2 (log):", r2_log)



# ----------------------------------------
# Improving the Housing Price Model: Model comparisons

# ----------------------------------------
	# Step 1: Import Libraries
	import pandas as pd
	import numpy as np
	from sklearn.model_selection import train_test_split
	from sklearn.metrics import mean_absolute_error, r2_score
	from sklearn.linear_model import LinearRegression, Ridge
	from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
	import matplotlib.pyplot as plt
	
	# Step 2: Load the Dataset
	data = pd.read_csv("ames_encoded.csv")
	
	# Step 3: Split into Features (X) and Target (y)
	X = data.drop("SalePrice", axis=1)
	y = data["SalePrice"]
	
	# Step 4: Train-Test Split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


  # Strategy 1: Linear Regression (Baseline)

	model = LinearRegression()
	model.fit(X_train, y_train)
	y_pred = model.predict(X_test)
	mae = mean_absolute_error(y_test, y_pred)
	r2 = r2_score(y_test, y_pred)
	
	print("Mean Absolute Error:", round(mae))
	print("R^2 Score:", round(r2, 2))
    
    
    
  #Strategy 2: Random Forest Regressor
  	model = RandomForestRegressor(n_estimators=100, random_state=42)
	model.fit(X_train, y_train)
	y_pred = model.predict(X_test)
	mae = mean_absolute_error(y_test, y_pred)
	r2 = r2_score(y_test, y_pred)
	
	print("Mean Absolute Error:", round(mae))
	print("R^2 Score:", round(r2, 2))
    
    
   # Strategy 3: Gradient Boosting Regressor
   
    model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
	model.fit(X_train, y_train)
	y_pred = model.predict(X_test)
	mae = mean_absolute_error(y_test, y_pred)
	r2 = r2_score(y_test, y_pred)
	
	print("Mean Absolute Error:", round(mae))
	print("R^2 Score:", round(r2, 2))
    
   # Strategy 4: Ridge Regression with Log-Transformed Target
   
     	y_log = np.log(y)
	
	X_train_log, X_test_log, y_train_log, y_test_log = train_test_split(X, y_log, test_size=0.2, random_state=42)
	
	model = Ridge()
	model.fit(X_train_log, y_train_log)
	pred_log = model.predict(X_test_log)
	y_pred = np.exp(pred_log)
	mae = mean_absolute_error(y_test, y_pred)
	r2 = r2_score(y_test, y_pred)
	
	print("Mean Absolute Error:", round(mae))
	print("R^2 Score:", round(r2, 2))
   
    

# ----------------------------------------
# Create Comparison Plots MAE and R^2

# ----------------------------------------

import matplotlib.pyplot as plt
	
models = ['Linear', 'Random Forest', 'Gradient Boosting', 'Ridge (log)']
mae_scores = [21622, 17969, 17561, 17721]
r2_scores = [0.85, 0.88, 0.90, 0.90]

# Plot MAE
plt.figure(figsize=(8, 4))
plt.bar(models, mae_scores, color='skyblue')
plt.ylabel("Mean Absolute Error ($)")
plt.title("Model Comparison: MAE")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("model_comparison_mae.png")
plt.show()

# Plot R Square
plt.figure(figsize=(8, 4))
plt.bar(models, r2_scores, color='lightgreen')
plt.ylabel("R Square Score")
plt.title("Model Comparison: R Square Score")
plt.xticks(rotation=15)
plt.ylim(0.80, 0.95)
plt.tight_layout()
plt.savefig("model_comparison_r2.png")
plt.show()


# ----------------------------------------
# Create scatter plot for actual vs predicted: Gradient Boosting

# ----------------------------------------
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred, alpha=0.5, color="steelblue")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Actual SalePrice ($)")
plt.ylabel("Predicted SalePrice ($)")
plt.title("Gradient Boosting: Actual vs Predicted Prices")
plt.tight_layout()
plt.savefig("actual_vs_predicted_gradient.png")
plt.show()  # Display the plot
