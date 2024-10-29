from model.model import Inventory, FoodItem
from view.view import FoodView

class FoodController:
    def __init__(self):
        self.inventory = Inventory()
        self.view = FoodView()

    def run(self):
        while True:
            self.view.display_menu()
            choice = input("Choose an option: ")
            
            if choice == "1":  # Add Item
                name, category, quantity, price, expiration_date = self.view.prompt_for_food_details()
                item = FoodItem(name, category, quantity, price, expiration_date)
                self.inventory.add_item(item)
                print("Item added successfully.")
            
            elif choice == "2":  # Remove Item
                item_name = input("Enter the name of the item to remove: ")
                if self.inventory.remove_item(item_name):
                    print("Item removed successfully.")
                else:
                    print("Item not found.")
            
            elif choice == "3":  # View All Items
                self.view.display_all_items(self.inventory.food_items)
            
            elif choice == "4":  # View Near Expiration Items
                near_expiration_items = self.inventory.get_near_expiration_items()
                self.view.display_near_expiration_items(near_expiration_items)
            
            elif choice == "5":  # View Total Inventory Value
                total_value = self.inventory.get_total_value()
                self.view.display_total_value(total_value)
            
            elif choice == "6":  # Search Item
                keyword, category = self.view.prompt_for_search()
                search_results = self.inventory.search_items(keyword, category)
                self.view.display_search_results(search_results)
            
            elif choice == "7":  # View Inventory History
                history = self.inventory.history.get_history()
                self.view.display_history(history)
            
            elif choice == "8":  # Import Data
                filename = self.view.prompt_for_filename()
                self.inventory.import_data(filename)
            
            elif choice == "9":  # Export Data
                filename = self.view.prompt_for_filename()
                self.inventory.export_data(filename)
            
            elif choice == "0":  # Exit
                print("Exiting the program. Goodbye!")
                break
            
            else:
                print("Invalid option. Please try again.")