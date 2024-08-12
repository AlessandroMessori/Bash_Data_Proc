import pandas as pd

# Read the CSV file
df = pd.read_csv('./data_4.csv')

# Data cleaning and preprocessing
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'].astype(str).replace("Ten", 10).replace("Two", 2), errors='coerce')
df["OrderDate"] = pd.to_datetime(df["OrderDate"], format="mixed")

# Calculate total sales by region
df['Total Sales'] = df['Quantity'] * df['Price']
total_sales_by_region = df[~df["Total Sales"].isna()].groupby('Region')['Total Sales'].sum()

# Calculate average price per product
average_price_per_product = df[~df["Price"].isna()].groupby('Product')['Price'].mean()

# Calculate sold products per day
sold_products_per_day = df[~df["Quantity"].isna()].groupby('OrderDate')['Quantity'].su
m()

# Output the results
print("Total Sales by Region:\n", total_sales_by_region)
print("Average Price per Product:\n", average_price_per_product)
print("Sold Products per Day\n", sold_products_per_day)
