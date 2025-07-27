# ----------------------------------------
# Load Libraries for Machine Learning
# ----------------------------------------

import pandas as pd  # pandas helps us load and manage tabular data (like spreadsheets)
from sklearn.model_selection import train_test_split  # splits our data into training and testing sets
from sklearn.preprocessing import LabelEncoder  # turns words into numbers for machine learning
from sklearn.ensemble import RandomForestClassifier  # a powerful model that uses many decision trees
from sklearn.linear_model import LogisticRegression  # a simpler model that works well for binary tasks
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report  # helps us evaluate how well our model did
import matplotlib.pyplot as plt  # lets us draw charts to understand the results better

# ----------------------------------------
# Load and Prepare the Dataset
# ----------------------------------------

# Load a dataset with customer purchase history
# Make sure this file is in the same folder as your script
df = pd.read_csv("customer_purchases_balanced.csv")

# Create a new column that is True (1) if the product is "Electronics", otherwise False (0)
df["IsElectronics"] = (df["ProductCategory"] == "Electronics").astype(int)

# ----------------------------------------
# Select Features and Target
# ----------------------------------------

# Features = input data used to predict (like Age, Gender, etc.)
# Target = what we want to predict (whether it's Electronics or not)
X = df[["Age", "Gender", "City", "PaymentMethod"]].copy()
y = df["IsElectronics"]

# Convert text values to numbers (e.g., Male/Female -> 0/1)
encoders = {}
for col in ["Gender", "City", "PaymentMethod"]:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])  # Transform column
    encoders[col] = le  # Save encoder so we can decode predictions later

# ----------------------------------------
# Train-Test Split
# ----------------------------------------

# We split the dataset into training (70%) and test (30%) to evaluate performance
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ----------------------------------------
# Train Random Forest Model
# ----------------------------------------

# Build and train a Random Forest model on the training data
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# ----------------------------------------
# Make Predictions and Evaluate Model
# ----------------------------------------

# Predict on the test data
y_pred = model.predict(X_test)

# Print confusion matrix (how many correct/incorrect predictions)
print("=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred))

# Print precision, recall, and F1-score for each class
print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred))

# ----------------------------------------
# Try Logistic Regression Instead
# ----------------------------------------

# Try a different model and compare its results
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
log_pred = log_model.predict(X_test)

print("\n=== Logistic Regression Report ===")
print(classification_report(y_test, log_pred))

# ----------------------------------------
# Mini Challenge: Use Only Age and Gender
# ----------------------------------------

# What if we used fewer features? Let's try only Age and Gender
X_challenge = df[["Age", "Gender"]].copy()
X_challenge["Gender"] = encoders["Gender"].transform(X_challenge["Gender"])

# Split again
X_train_ch, X_test_ch, y_train_ch, y_test_ch = train_test_split(
    X_challenge, y, test_size=0.3, random_state=1
)

# Train and evaluate a smaller model
mini_model = RandomForestClassifier(random_state=1)
mini_model.fit(X_train_ch, y_train_ch)
y_pred_ch = mini_model.predict(X_test_ch)

print("\n=== Mini Challenge Classification Report ===")
print(classification_report(y_test_ch, y_pred_ch))

# ----------------------------------------
# Visualize: Predicted vs Actual
# ----------------------------------------

# Draw a bar chart comparing real vs predicted outcomes
compare_df = pd.DataFrame({"Actual": y_test_ch, "Predicted": y_pred_ch})
counts = compare_df.value_counts().unstack()
counts.index = ["Not Electronics (False)", "Electronics (True)"]
counts.plot(kind="bar", color=["skyblue", "orange"])
plt.title("Predicted vs Actual: Electronics Purchase")
plt.xlabel("Actual Class")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ----------------------------------------
# Final Project: Predict New Customers
# ----------------------------------------

# Let's test our model on new, unseen customers
new_customers = pd.DataFrame({
    "Age": [25, 37, 52, 30, 46],
    "Gender": ["Female", "Male", "Male", "Female", "Female"],
    "City": ["London", "Manchester", "Leeds", "Bristol", "London"],
    "PaymentMethod": ["Card", "PayPal", "Cash", "PayPal", "Cash"]
})

# Only keep rows with values we've seen before (to avoid encoding errors)
for col in ["Gender", "City", "PaymentMethod"]:
    known = set(encoders[col].classes_)
    new_customers = new_customers[new_customers[col].isin(known)]

# Apply the same encoders to the new customer data
for col in ["Gender", "City", "PaymentMethod"]:
    new_customers[col] = encoders[col].transform(new_customers[col])

# Predict whether each new customer will buy Electronics
new_predictions = model.predict(new_customers)
new_customers["Predicted_Electronics"] = new_predictions

# ----------------------------------------
# Show Results in Human-Friendly Format
# ----------------------------------------

# Print predicted Electronics buyers
buyers = new_customers[new_customers["Predicted_Electronics"] == 1]
non_buyers = new_customers[new_customers["Predicted_Electronics"] == 0]

print("\n=== Customers Predicted to Buy Electronics ===")
for i, row in buyers.iterrows():
    print(f"Customer {i+1}: Age {row['Age']}, Gender {encoders['Gender'].inverse_transform([row['Gender']])[0]}, "
          f"City {encoders['City'].inverse_transform([row['City']])[0]}, "
          f"Payment Method {encoders['PaymentMethod'].inverse_transform([row['PaymentMethod']])[0]}")

# Print predicted Non-buyers
print("\n=== Customers Not Predicted to Buy Electronics ===")
for i, row in non_buyers.iterrows():
    print(f"Customer {i+1}: Age {row['Age']}, Gender {encoders['Gender'].inverse_transform([row['Gender']])[0]}, "
          f"City {encoders['City'].inverse_transform([row['City']])[0]}, "
          f"Payment Method {encoders['PaymentMethod'].inverse_transform([row['PaymentMethod']])[0]}")
