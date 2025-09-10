import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file (replace 'data.csv' with your file)
file_path = "data.csv"
try:
    data = pd.read_csv(file_path)
    print("✅ Data loaded successfully!\n")
except FileNotFoundError:
    print("❌ CSV file not found. Please place 'data.csv' in the same folder.")
    exit()

# Display first 5 rows
print("📌 First 5 Rows of Data:")
print(data.head(), "\n")

# Basic Info
print("📊 Dataset Info:")

print(data.info(), "\n")

# Summary Statistics
print("📈 Summary Statistics:")
print(data.describe(), "\n")

# Example Visualization - Histogram for all numeric columns
data.hist(figsize=(10, 6), bins=20, edgecolor='black')
plt.suptitle("Histograms of Numeric Columns")
plt.show()

# Scatter Plot Example (if numeric columns exist)
numeric_cols = data.select_dtypes(include="number").columns
if len(numeric_cols) >= 2:
    plt.figure(figsize=(7, 5))
    plt.scatter(data[numeric_cols[0]], data[numeric_cols[1]], alpha=0.6)
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    plt.title(f"Scatter Plot: {numeric_cols[0]} vs {numeric_cols[1]}")
    plt.show()
else:
    print("⚠️ Not enough numeric columns for scatter plot.")
