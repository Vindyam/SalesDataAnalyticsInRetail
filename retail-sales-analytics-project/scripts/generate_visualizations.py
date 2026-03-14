import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/retail_sales_dataset.csv")

date_col = "Date"
gender_col = "Gender"
age_col = "Age"
category_col = "Product Category"
quantity_col = "Quantity"
total_col = "Total Amount"

if date_col:
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

def save_plot(filename):
    plt.tight_layout()
    plt.savefig(f"../visualizations/{filename}", dpi=150, bbox_inches="tight")
    plt.close()

if category_col and total_col:
    s = df.groupby(category_col)[total_col].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    s.plot(kind="bar")
    plt.title("Sales by Product Category")
    plt.xlabel(category_col)
    plt.ylabel(total_col)
    save_plot("sales_by_category.png")

if gender_col and total_col:
    s = df.groupby(gender_col)[total_col].sum().sort_values(ascending=False)
    plt.figure(figsize=(7, 5))
    s.plot(kind="bar")
    plt.title("Sales by Gender")
    plt.xlabel(gender_col)
    plt.ylabel(total_col)
    save_plot("sales_by_gender.png")

if age_col:
    plt.figure(figsize=(8, 5))
    pd.to_numeric(df[age_col], errors="coerce").dropna().plot(kind="hist", bins=20)
    plt.title("Customer Age Distribution")
    plt.xlabel(age_col)
    plt.ylabel("Frequency")
    save_plot("age_distribution.png")

if date_col and total_col:
    monthly = (
        df.dropna(subset=[date_col])
        .assign(month=df[date_col].dt.to_period("M").astype(str))
        .groupby("month")[total_col]
        .sum()
    )
    if len(monthly) > 0:
        plt.figure(figsize=(9, 5))
        monthly.plot(kind="line", marker="o")
        plt.title("Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel(total_col)
        plt.xticks(rotation=45, ha="right")
        save_plot("monthly_sales_trend.png")

if category_col and quantity_col:
    s = df.groupby(category_col)[quantity_col].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    s.plot(kind="bar")
    plt.title("Units Sold by Category")
    plt.xlabel(category_col)
    plt.ylabel(quantity_col)
    save_plot("units_sold_by_category.png")

print("Visualizations generated in ../visualizations/")
