import pandas as pd

df = pd.read_csv("../data/retail_sales_dataset.csv")

print("Original shape:", df.shape)
print("\nMissing values:")
print(df.isna().sum())

df = df.drop_duplicates()

# Basic type handling
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print("\nCleaned shape:", df.shape)

df.to_csv("../data/retail_sales_cleaned.csv", index=False)
print("Saved cleaned dataset to ../data/retail_sales_cleaned.csv")
