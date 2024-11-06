import re

class HouseView:
    @staticmethod
    def display_menu():
        print("\nWelcome to the Rent Houses Application")
        print("1. View all houses")
        print("2. Add new house")
        print("3. Remove house")
        print("4. Exit")
        print("=".center(50, "="))

    @staticmethod
    def display_houses(houses):
        if not houses:
            print("There are no houses available.")
        else:
            for house in houses:
                print(house)

    @staticmethod
    def get_house_details():
        address = input("Enter house address: ")
        rent = HouseView.validate_rent()
        bedrooms = HouseView.validate_bedrooms()
        bathrooms = HouseView.validate_bathrooms()

        return address, rent, bedrooms, bathrooms

    @staticmethod
    def validate_rent():
        while True:
            try:
                rent = float(input("Enter rent amount: "))
                return rent
            except ValueError:
                print("Error: Rent must be a valid number. Please try again.")

    @staticmethod
    def validate_bedrooms():
        while True:
            try:
                bedrooms = int(input("Enter number of bedrooms: "))
                return bedrooms
            except ValueError:
                print("Error: Number of bedrooms must be a valid integer. Please try again.")

    @staticmethod
    def validate_bathrooms():
        while True:
            try:
                bathrooms = int(input("Enter number of bathrooms: "))
                return bathrooms
            except ValueError:
                print("Error: Number of bathrooms must be a valid integer. Please try again.")

    @staticmethod
    def display_success_message(message):
        print(f"Success: {message}")

    @staticmethod
    def display_error_message(message):
        print(f"Error: {message}")

    @staticmethod
    def get_house_id():
        while True:
            try:
                house_id = int(input("Enter the house ID to remove: "))
                return house_id
            except ValueError:
                print("Error: ID must be a valid integer. Please try again.")