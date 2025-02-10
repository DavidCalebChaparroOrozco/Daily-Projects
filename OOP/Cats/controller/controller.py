from model.model import CatModel
from view.view import CatView

# Handles user interactions and business logic
class CatController:
    def __init__(self, model: CatModel, view: CatView):
        self.model = model
        self.view = view

    # Displays all cats
    def view_all_cats(self):
        cats = self.model.get_all_cats()
        self.view.display_cats(cats)

    # Adds a new cat to the system
    def add_cat(self, name, breed, age):
        self.model.add_cat(name, breed, age)
        self.model.calculate_statistics()
        self.view.display_message(f"✅ Cat '{name}' added successfully!")

    # Removes a cat by name
    def remove_cat(self, name):
        if self.model.remove_cat(name):
            self.model.calculate_statistics()
            self.view.display_message(f"🗑️ Cat '{name}' removed successfully!")
        else:
            self.view.display_message(f"❌ Cat '{name}' not found!")

    # Searches for cats by breed
    def search_by_breed(self, breed):
        cats = self.model.filter_by_breed(breed)
        if cats:
            self.view.display_cats([(cat.name, cat.breed, cat.age) for cat in cats])
        else:
            self.view.display_message(f"❌ No cats found for breed '{breed}'")

    # Updates a cat's age
    def update_cat_age(self, name, new_age):
        if self.model.update_age(name, new_age):
            self.model.calculate_statistics()
            self.view.display_message(f"📝 Updated '{name}' age to {new_age} years!")
        else:
            self.view.display_message(f"❌ Cat '{name}' not found!")

    # Shows system statistics
    def show_statistics(self):
        self.model.calculate_statistics()
        self.view.display_statistics(self.model.stats)

    # Saves data to a file
    def save_to_file(self):
        self.model.save_data()
        self.view.display_message("💾 Data saved successfully!")

    # Loads data from a file
    def load_from_file(self):
        self.model.load_data()
        self.model.calculate_statistics()
        self.view.display_message("📂 Data loaded successfully!")

    # Visualize data
    def visualize_data(self):
        self.model.visualize_data()