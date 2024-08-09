import pandas as pd

df = pd.read_csv("./data/nse_all_stock_data.csv")

print(df.isna().sum())

print(len(df))
