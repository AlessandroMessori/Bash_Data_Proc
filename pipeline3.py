import pandas as pd

# Read the CSV file
df = pd.read_csv('data_2.csv')

# Data cleaning and preprocessing
df['Experience'] = df['Experience'].str.replace("Two", "2").astype(int)

# Convert 'Date of Joining' to datetime
df['Date of Joining'] = pd.to_datetime(df["Date of Joining"], format="mixed")

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# Calculate total salary by department
total_salary_by_department = df[~df["Salary"].isna()].groupby('Department')['Salary'].sum()

# Calculate average experience by department
average_experience_by_department = df.groupby('Department')['Experience'].mean()

# Output the results
print("Total Salary by Department:\n", total_salary_by_department)
print("Average Experience by Department:\n", average_experience_by_department)
