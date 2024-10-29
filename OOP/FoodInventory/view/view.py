class FoodView:
    @staticmethod
    def display_menu():
        print("\nFood Inventory Management System")
        print("1. Add Food Item")
        print("2. Remove Food Item")
        print("3. View All Items")
        print("4. View Near Expiration Items")
        print("5. View Total Inventory Value")
        print("6. Search Food Item")
        print("7. View Inventory History")
        print("8. Import Data")
        print("9. Export Data")
        print("0. Exit")

    @staticmethod
    def prompt_for_food_details():
        name = input("Enter food name: ")
        category = input("Enter category (e.g., Fruit, Vegetable): ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))
        expiration_date = input("Enter expiration date (YYYY-MM-DD) or leave blank: ")
        
        return name.strip(), category.strip(), quantity, price, expiration_date.strip()

    @staticmethod
    def display_all_items(food_items):
        print("\nAll Food Items:")
        for item in food_items:
            expiration_info = f"Expires in {item.days_until_expired()} days" if not item.is_expired() else "Expired"
            print(f"{item.name} - {item.category} - Quantity: {item.quantity} - Price: ${item.price:.2f} - {expiration_info}")

    @staticmethod
    def display_near_expiration_items(food_items):
        print("\nItems Near Expiration:")
        for item in food_items:
            print(f"{item.name} - Expires in {item.days_until_expired()} days")

    @staticmethod
    def display_total_value(value):
        print(f"\nTotal Inventory Value: ${value:.2f}")

    @staticmethod
    def prompt_for_search():
        keyword = input("Enter keyword to search: ")
        category = input("Enter category (or leave blank): ")
        
        return keyword.strip(), category.strip()

    @staticmethod
    def display_search_results(items):
        print("\nSearch Results:")
        for item in items:
            print(f"{item.name} - {item.category} - Quantity: {item.quantity} - Price: ${item.price:.2f}")

    @staticmethod
    def display_history(history):
        print("\nInventory History:")
        for record in history:
            print(f"{record['date']} - {record['action'].capitalize()} {record['quantity']} of {record['item_name']}")

    @staticmethod
    def prompt_for_filename():
        return input("Enter filename: ").strip()