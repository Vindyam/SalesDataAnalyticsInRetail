# Retail Sales Data Analysis

## Overview
This project analyzes a retail sales dataset to identify sales patterns, customer behavior, and product performance. It is designed as a portfolio-ready **Data Analytics** project for GitHub and demonstrates skills in:

- data cleaning
- exploratory data analysis
- data visualization
- business insight generation
- notebook-based storytelling

## Dataset Summary
- Rows: **1,000**
- Columns: **9**

### Available Columns
- `Transaction ID`
- `Date`
- `Customer ID`
- `Gender`
- `Age`
- `Product Category`
- `Quantity`
- `Price per Unit`
- `Total Amount`

## Business Questions
This project answers questions such as:
1. What is the overall sales performance?
2. Which product categories generate the most revenue?
3. Are there spending differences across customer segments?
4. How does age relate to purchasing behavior?
5. What trends can be observed over time?

## Project Structure
```text
retail-sales-analytics-project/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── retail_sales_dataset.csv
├── notebooks/
│   └── retail_sales_analysis.ipynb
├── scripts/
│   ├── data_cleaning.py
│   └── generate_visualizations.py
├── visualizations/
│   ├── sales_by_category.png
sales_by_gender.png
age_distribution.png
monthly_sales_trend.png
units_sold_by_category.png
top_10_customers_by_sales.png
average_spend_by_age_group.png
├── outputs/
│   ├── dataset_profile.txt
│   └── key_insights.md
```

## Visualizations Included
- `sales_by_category.png`
- `sales_by_gender.png`
- `age_distribution.png`
- `monthly_sales_trend.png`
- `units_sold_by_category.png`
- `top_10_customers_by_sales.png`
- `average_spend_by_age_group.png`

## Key Insights
- Total recorded sales are 456,000.00 based on the `Total Amount` field.
- The top product category by sales is `Electronics` with sales of 156,905.00.
- The higher-spending gender segment in this dataset is `Female` with total sales of 232,840.00.
- The age group with the highest average spend is `<=18` at 534.05 per transaction on average.

## Tools Used
- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## How to Run
### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the notebook
```bash
jupyter notebook notebooks/retail_sales_analysis.ipynb
```

### 3. Or regenerate visuals with the script
```bash
python scripts/generate_visualizations.py
```

## GitHub Upload
After unzipping the project, push it to GitHub with:

```bash
git init
git add .
git commit -m "Add retail sales analytics portfolio project"
git branch -M main
git remote add origin https://github.com/YOURUSERNAME/retail-sales-analytics-project.git
git push -u origin main
```

## Portfolio Positioning
This project is suitable for a **Data Analyst** portfolio because it emphasizes data preparation, visual analysis, and business-oriented interpretation rather than only model building.
