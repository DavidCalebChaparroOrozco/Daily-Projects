# Importing necessary libraries
import json
from datetime import datetime

# Class representing a Christmas gift.
class Gift:
    
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category
        # Store date added as ISO format string
        self.date_added = datetime.now().isoformat()  

    # Return a string representation of the gift.
    def __str__(self):
        return f"{self.name} (Category: {self.category}) - {self.description} (Added on: {self.date_added})"

    # Convert gift to dictionary for JSON serialization.
    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'date_added': self.date_added,
        }

    @staticmethod
    # Create a Gift instance from a dictionary.
    def from_dict(data):
        return Gift(data['name'], data['description'], data['category'])


# Model to manage the list of gifts.
class GiftModel:
    
    def __init__(self):
        self.gifts = []
        self.load_gifts()

    # Add a new gift to the list.
    def add_gift(self, gift):
        self.gifts.append(gift)
        self.save_gifts()

    # Remove a gift from the list by name.
    def remove_gift(self, gift_name):
        self.gifts = [gift for gift in self.gifts if gift.name != gift_name]
        self.save_gifts()

    # Update an existing gift's information.
    def update_gift(self, old_name, new_gift):
        for idx, gift in enumerate(self.gifts):
            if gift.name == old_name:
                self.gifts[idx] = new_gift
                break
        self.save_gifts()

    # Return the list of all gifts.
    def get_all_gifts(self):
        return self.gifts

    # Save the current list of gifts to a JSON file.
    def save_gifts(self):
        with open('gifts.json', 'w') as f:
            json.dump([gift.to_dict() for gift in self.gifts], f)

    # Load gifts from a JSON file.
    def load_gifts(self):
        try:
            with open('gifts.json', 'r') as f:
                gifts_data = json.load(f)
                self.gifts = [Gift.from_dict(gift) for gift in gifts_data]
        except FileNotFoundError:
            # Start with an empty list if file does not exist
            self.gifts = []  

    # Search for gifts by name or description.
    def search_gift(self, keyword):
        return [gift for gift in self.gifts if keyword.lower() in gift.name.lower() or keyword.lower() in gift.description.lower()]

    # Sort gifts by specified key (name, category, date_added).
    def sort_gifts(self, key):
        if key == "name":
            return sorted(self.gifts, key=lambda x: x.name)
        elif key == "category":
            return sorted(self.gifts, key=lambda x: x.category)
        elif key == "date_added":
            return sorted(self.gifts, key=lambda x: x.date_added)
