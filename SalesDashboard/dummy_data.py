# Import necessary libraries
import random
import csv
from datetime import datetime, timedelta
import os

# Seed for reproducibility
random.seed(50)

# Generate dummy data
categories = ['Electronics', 'Clothing', 'Furniture', 'Groceries', 'Toys']
products = {
    'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Monitor'],
    'Clothing': ['Shirt', 'Pants', 'Jacket', 'Shoes', 'Dress'],
    'Furniture': ['Chair', 'Table', 'Couch', 'Desk', 'Bookshelf'],
    'Groceries': ['Apple', 'Milk', 'Bread', 'Eggs', 'Cheese'],
    'Toys': ['Action Figure', 'Board Game', 'Doll', 'Puzzle', 'Toy Car']
}
date_start = datetime(2024, 1, 1)
date_end = datetime(2025, 1, 31)

# Generate 50 dummy entries
data = []
for _ in range(50):
    category = random.choice(categories)
    product = random.choice(products[category])
    # Amount between 10 and 2000
    amount = random.randint(10, 2000)  
    random_date = date_start + timedelta(days=random.randint(0, (date_end - date_start).days))
    data.append([random_date.strftime('%Y-%m-%d'), category, product, amount])

# Save data to CSV
directory = 'data'
filename = "sales.csv"

# Create the directory if it does not exist
os.makedirs(directory, exist_ok=True)

# Save data to CSV
file_path = os.path.join(directory, filename)
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Header
    writer.writerow(['date', 'category', 'product', 'amount'])  
    writer.writerows(data)

print(f'Data saved successfully to {file_path}')