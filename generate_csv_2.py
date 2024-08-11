import csv
import random

# Generate a CSV file with random data
def generate_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['column1', 'column2', 'column3']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(10):
            writer.writerow({
                'column1': random.randint(1, 100),
                'column2': random.uniform(0, 1),
                'column3': random.choice(['A', 'B', 'C'])
            })


generate_csv("./data/random_data.csv")
