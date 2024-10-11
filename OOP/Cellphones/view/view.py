class View:
    @staticmethod
    def display_menu():
        # Displays the menu options to the user
        print("\n--- Cellphone Inventory Management ---")
        print("1. Add New Cellphone")
        print("2. Update Stock")
        print("3. View All Cellphones")
        print("4. Exit")

    @staticmethod
    def get_user_choice():
        # Gets the user's menu selection
        return input("Enter your choice: ")

    @staticmethod
    def get_cellphone_details():
        # Prompts user for cellphone details
        model_name = input("Enter model name: ")
        brand = input("Enter brand: ")
        stock = input("Enter stock quantity: ")

        # Input validation to ensure stock is numeric
        while not stock.isdigit():
            print("Stock must be a number.")
            stock = input("Enter stock quantity: ")

        return model_name, brand, int(stock)

    @staticmethod
    def get_model_name():
        # Gets the cellphone model name for search or update
        return input("Enter the model name to search: ")

    @staticmethod
    def get_new_stock():
        # Gets the updated stock quantity
        new_stock = input("Enter the new stock quantity: ")

        # Input validation to ensure stock is numeric
        while not new_stock.isdigit():
            print("Stock must be a number.")
            new_stock = input("Enter the new stock quantity: ")

        return int(new_stock)

    @staticmethod
    def display_cellphones(cellphones):
        # Displays all cellphones in the inventory
        if cellphones:
            print("\n--- Cellphone Inventory ---")
            for phone in cellphones:
                print(f"Model: {phone.get_model_name()}, Brand: {phone.get_brand()}, Stock: {phone.get_stock()}")
        else:
            print("No cellphones available in the inventory.")
    
    @staticmethod
    def show_message(message):
        # Displays a custom message
        print(message)
