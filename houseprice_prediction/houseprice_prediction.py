import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset (replace with Kaggle dataset or sample_data.csv)
file_path = "house_prices.csv"
try:
    data = pd.read_csv(file_path)
    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ CSV file not found. Please place 'house_prices.csv' in the folder.")
    exit()

# Display first few rows
print("📌 First 5 Rows:")
print(data.head(), "\n")

# Check for missing values
print("🔎 Missing Values:")
print(data.isnull().sum(), "\n")

# Select features (you can adjust based on dataset)
# Example: SquareFeet, Bedrooms, Bathrooms → Price
features = ["SquareFeet", "Bedrooms", "Bathrooms"]
target = "Price"

# Drop rows with NaN in required columns
data = data.dropna(subset=features + [target])

X = data[features]
y = data[target]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model Evaluation
print("📊 Model Evaluation:")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")
print(f"R² Score: {r2_score(y_test, y_pred):.2f}\n")

# Predict on new data
sample_house = np.array([[2000, 3, 2]])  # Example: 2000 sqft, 3 bed, 2 bath
predicted_price = model.predict(sample_house)
print(f"💰 Predicted Price for {sample_house[0]}: {predicted_price[0]:.2f}")
