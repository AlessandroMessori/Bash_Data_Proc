import pandas as pd
import csv

# Data pipeline with potential issues
def process_data(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    # Data cleaning and transformation (potential issues)
    cleaned_data = []
    for row in data:
        cleaned_data.append({
            'column1': int(row['column1']),
            'column2': float(row['column2']),
            'column3': row['column3']
        })

    # Analysis (potential issues)
    average_column1 = sum(row['column1'] for row in cleaned_data) / len(cleaned_data)
    count_column3_A = sum(1 for row in cleaned_data if row['column3'] == 'A')

    print(f"Average of column1: {average_column1}")
    print(f"Count of column3 with value 'A': {count_column3_A}")


process_data("./random_data.csv")
