class BakeryView:
    @staticmethod
    def display_menu():
        print("\nWelcome to the Bakery Management System")
        print("1. View all items")
        print("2. Add new item")
        print("3. Remove item")
        print("4. Update item")
        print("5. Search item by name")
        print("6. Display total inventory value")
        print("7. Exit")
        print("=".center(50, "="))

    @staticmethod
    def display_items(items):
        if not items:
            print("There are no bakery items available.")
        else:
            for index, item in enumerate(items):
                print(f"{index}: {item}")

    @staticmethod
    def get_item_details():
        name = input("Enter item name: ")
        price = BakeryView.validate_price()
        quantity = BakeryView.validate_quantity()
        
        return name, price, quantity

    @staticmethod
    def get_update_details():
        name = input("Enter new item name (leave blank to keep current): ")
        price = BakeryView.validate_price()
        quantity = BakeryView.validate_quantity()
        
        return name, price, quantity

    @staticmethod
    def validate_price():
        while True:
            try:
                price = float(input("Enter item price: "))
                return price
            except ValueError:
                print("Error: Price must be a valid number. Please try again.")

    @staticmethod
    def validate_quantity():
        while True:
            try:
                quantity = int(input("Enter item quantity: "))
                return quantity
            except ValueError:
                print("Error: Quantity must be a valid integer. Please try again.")

    @staticmethod
    def display_success_message(message):
        print(f"Success: {message}")

    @staticmethod
    def display_error_message(message):
        print(f"Error: {message}")

    @staticmethod
    def get_item_index():
        while True:
            try:
                index = int(input("Enter the item index to remove or update: "))
                return index
            except ValueError:
                print("Error: Index must be a valid integer. Please try again.")

    @staticmethod
    def get_item_name():
        return input("Enter the name of the item to search for: ")

    @staticmethod
    def display_total_value(total_value):
        print(f"Total inventory value: ${total_value:.2f}")