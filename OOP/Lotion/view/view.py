class LotionView:
    @staticmethod
    def display_menu():
        print("\nWelcome to the Lotion Store")
        print("1. View all lotions")
        print("2. Add new lotion")
        print("3. Remove lotion")
        print("4. Update lotion stock")
        print("5. Exit")

    @staticmethod
    def display_lotions(lotions):
        if not lotions:
            print("No lotions available.")
        else:
            for lotion in lotions:
                print(lotion)

    @staticmethod
    def get_lotion_details():
        lotion_id = input("Enter Lotion ID: ")
        name = input("Enter Lotion Name: ")
        brand = input("Enter Brand: ")
        price = float(input("Enter Price: "))
        stock = int(input("Enter Stock: "))
        return lotion_id, name, brand, price, stock

    @staticmethod
    def get_lotion_id():
        return input("Enter the Lotion ID to remove: ")

    @staticmethod
    def get_lotion_stock_update():
        lotion_id = input("Enter Lotion ID to update stock: ")
        new_stock = int(input("Enter new stock quantity: "))
        return lotion_id, new_stock

    @staticmethod
    def display_success_message(message):
        print(f"Success: {message}")

    @staticmethod
    def display_error_message(message):
        print(f"Error: {message}")