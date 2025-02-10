import json
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# Represents a cat entity
class Cat:
    def __init__(self, name, breed, age):
        if not name or not breed or age <= 0:
            raise ValueError("Invalid cat data: Name and breed must be non-empty, and age must be positive.")
        self.name = name
        self.breed = breed
        self.age = age

# Manages data storage and operations
class CatModel:
    def __init__(self):
        self.cats = []
        self.stats = {'total_cats': 0, 'average_age': 0.0, 'most_common_breed': ''}

    # Calculates system statistics
    def calculate_statistics(self):
        if not self.cats:
            self.stats = {'total_cats': 0, 'average_age': 0.0, 'most_common_breed': ''}
            return
        
        total_age = sum(cat.age for cat in self.cats)
        breed_count = Counter(cat.breed for cat in self.cats)
        
        self.stats['total_cats'] = len(self.cats)
        self.stats['average_age'] = total_age / len(self.cats)
        self.stats['most_common_breed'] = breed_count.most_common(1)[0][0]

    # Adds a new cat to storage
    def add_cat(self, name, breed, age):
        try:
            new_cat = Cat(name, breed, age)
            self.cats.append(new_cat)
            self.calculate_statistics()
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False

    # Removes a cat by name
    def remove_cat(self, name):
        for i, cat in enumerate(self.cats):
            if cat.name.lower() == name.lower():
                del self.cats[i]
                return True
        return False

    # Returns all cats
    def get_all_cats(self):
        return [(cat.name, cat.breed, cat.age) for cat in self.cats]

    # Filters cats by breed
    def filter_by_breed(self, breed):
        return [cat for cat in self.cats if cat.breed.lower() == breed.lower()]

    # Updates a cat's age
    def update_age(self, name, new_age):
        if new_age <= 0:
            print("Error: Age must be a positive number.")
            return False
        
        for cat in self.cats:
            if cat.name.lower() == name.lower():
                cat.age = new_age
                self.calculate_statistics()
                return True
        return False
    
    # Saves cat data to JSON file
    def save_data(self, filename='cat_data.json'):
        try:
            data = [{'name': cat.name, 'breed': cat.breed, 'age': cat.age} for cat in self.cats]
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    # Loads cat data from JSON file
    def load_data(self, filename='cat_data.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.cats = [Cat(item['name'], item['breed'], item['age']) for item in data]
            self.calculate_statistics()
            return True
        except FileNotFoundError:
            print("No previous data found. Starting fresh.")
            return False
        except Exception as e:
            print(f"Error loading data: {e}")
            return False

    # Visualizes cat data
    def visualize_data(self):
        if not self.cats:
            print("No data available for visualization.")
            return
        
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        fig.suptitle("Cat Data Visualization", fontsize=16, fontweight='bold')

        # Age Distribution
        ages = [cat.age for cat in self.cats]
        sns.histplot(ages, bins=10, kde=True, ax=axes[0], color="#64748b")
        axes[0].set_title("Age Distribution", fontsize=14)
        axes[0].set_xlabel("Age")
        axes[0].set_ylabel("Count")

        # Breed Count
        breed_count = Counter(cat.breed for cat in self.cats)
        sns.barplot(x=list(breed_count.keys()), y=list(breed_count.values()), ax=axes[1], palette="coolwarm")
        axes[1].set_title("Breed Count", fontsize=14)
        axes[1].set_xlabel("Breed")
        axes[1].set_ylabel("Count")
        axes[1].tick_params(axis='x', rotation=90)

        plt.tight_layout()
        plt.show()