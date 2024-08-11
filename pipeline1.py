import pandas as pd

# Step 1: Load the CSV file
file_path = 'path_to_your_csv/employees_with_issues.csv'
df = pd.read_csv(file_path)

# Step 2: Clean and preprocess the data
df['Age'] = pd.to_numeric(df['Age'])  # Convert Age to numeric
df['Salary'] = pd.to_numeric(df['Salary'])  # Convert Salary to numeric

# Step 3: Calculate average salary per department
avg_salary = df.groupby('Department')['Salary'].mean()

# Step 4: Identify individuals above a certain age
age_threshold = 30
above_threshold = df[df['Age'] > age_threshold]

# Step 5: Print results
print("Average Salary per Department:")
print(avg_salary)
print("\nIndividuals above age threshold:")
print(above_threshold)

