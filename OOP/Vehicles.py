# Importing necessary libraries
from abc import ABC, abstractmethod

# Base Class for Person (Owner and Manufacturer)
class Person(ABC):
    def __init__(self, name, id_number):
        # Encapsulation: Making attributes private
        self._name = name
        self._id_number = id_number

    @abstractmethod
    def get_description(self):
        """
        Abstract method to get the description of the person.
        Subclasses must implement this method.
        """
        pass

    # Getter method to retrieve the name of the person.
    def get_name(self):
        return self._name

    # Getter method to retrieve the ID number of the person.
    def get_id_number(self):
        return self._id_number


# Inheritance for Vehicle Owner
class VehicleOwner(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._vehicles_owned = []
        self._categories_subscribed = []

    # Implement the abstract method to get the description of the vehicle owner.
    def get_description(self):
        return f"Vehicle Owner: {self.get_name()} (ID: {self.get_id_number()})"

    # Method to subscribe to a vehicle category.
    def subscribe_category(self, category):
        self._categories_subscribed.append(category)

    # Method to get the list of vehicle categories the owner is subscribed to.
    def get_subscribed_categories(self):
        return self._categories_subscribed

    # Method to add a vehicle to the owner's list.
    def add_vehicle(self, vehicle):
        self._vehicles_owned.append(vehicle)

    # Method to get the list of vehicles owned by the owner.
    def get_vehicles_owned(self):
        return self._vehicles_owned


# Inheritance for Vehicle Manufacturer
class Manufacturer(Person):
    def __init__(self, name, id_number, company_name):
        super().__init__(name, id_number)
        self._company_name = company_name
        self._vehicles_manufactured = []

    # Implement the abstract method to get the description of the manufacturer.
    def get_description(self):
        return f"Manufacturer: {self.get_name()} (ID: {self.get_id_number()}), Company: {self._company_name}"

    # Method to add a vehicle to the manufacturer's portfolio.
    def add_vehicle(self, vehicle):
        self._vehicles_manufactured.append(vehicle)

    # Method to get the list of vehicles the manufacturer has developed.
    def get_manufactured_vehicles(self):
        return self._vehicles_manufactured


# Class for Vehicle
class Vehicle:
    def __init__(self, model, category, manufacturer, rating, release_year):
        self._model = model
        self._category = category
        self._manufacturer = manufacturer
        self._rating = rating
        self._release_year = release_year

    # Method to get the description of the vehicle.
    def get_description(self):
        return (f"Vehicle: {self._model} (Category: {self._category}, "
                f"Rating: {self._rating}/10, Released: {self._release_year}), "
                f"Manufactured by: {self._manufacturer.get_name()}")

    # Method to get the vehicle's category.
    def get_category(self):
        return self._category

    # Method to get the vehicle's release year.
    def get_release_year(self):
        return self._release_year


# Function to print vehicle details
def print_vehicle_details(vehicle):
    print(vehicle.get_description())


# Function to display the menu
def display_menu():
    print("\nVehicle Subscription System")
    print("1. Register new vehicle owner")
    print("2. Register new manufacturer")
    print("3. Register new vehicle")
    print("4. Subscribe owner to a vehicle category")
    print("5. Display vehicle owner details")
    print("6. Display vehicle details")
    print("7. Display manufacturer details")
    print("8. Exit")
    print("=".center(50, "="))
    return input("Select an option: ")


# Main code
if __name__ == "__main__":
    # Dictionary to hold vehicle owners
    owners = {}

    # Dictionary to hold manufacturers
    manufacturers = {}

    # Dictionary to hold vehicles
    vehicles = {}

    while True:
        option = display_menu()

        if option == "1":
            # Register new vehicle owner
            owner_name = input("Enter owner name: ")
            owner_id = input("Enter owner ID: ")
            if owner_id not in owners:
                owners[owner_id] = VehicleOwner(owner_name, owner_id)
                print("Vehicle owner registered successfully.")
            else:
                print("Owner ID already exists.")

        elif option == "2":
            # Register new manufacturer
            manufacturer_name = input("Enter manufacturer name: ")
            manufacturer_id = input("Enter manufacturer ID: ")
            company_name = input("Enter company name: ")
            if manufacturer_id not in manufacturers:
                manufacturers[manufacturer_id] = Manufacturer(manufacturer_name, manufacturer_id, company_name)
                print("Manufacturer registered successfully.")
            else:
                print("Manufacturer ID already exists.")

        elif option == "3":
            # Register new vehicle
            model = input("Enter vehicle model: ")
            category = input("Enter vehicle category (e.g., Sports, Minivan, Sedan): ")
            manufacturer_id = input("Enter manufacturer ID: ")
            if manufacturer_id in manufacturers:
                rating = float(input("Enter vehicle rating (0-10): "))
                release_year = int(input("Enter vehicle release year: "))
                manufacturer = manufacturers[manufacturer_id]
                vehicle = Vehicle(model, category, manufacturer, rating, release_year)
                vehicles[model] = vehicle
                manufacturer.add_vehicle(vehicle)
                print("Vehicle registered successfully.")
            else:
                print("Manufacturer ID not found.")

        elif option == "4":
            # Subscribe owner to a vehicle category
            owner_id = input("Enter owner ID: ")
            if owner_id in owners:
                category = input("Enter category to subscribe (e.g., Sports, Minivan, SUV): ")
                owner = owners[owner_id]
                owner.subscribe_category(category)
                print("Category subscription successful.")
            else:
                print("Owner ID not found.")

        elif option == "5":
            # Display vehicle owner details
            owner_id = input("Enter owner ID: ")
            if owner_id in owners:
                owner = owners[owner_id]
                print(owner.get_description())
                for category in owner.get_subscribed_categories():
                    print(f" - Subscribed to category: {category}")
                vehicles_owned = owner.get_vehicles_owned()
                if vehicles_owned:
                    print("Vehicles Owned:")
                    for vehicle in vehicles_owned:
                        print(f" - {vehicle.get_description()}")
            else:
                print("Owner not found.")

        elif option == "6":
            # Display vehicle details
            model = input("Enter vehicle model: ")
            if model in vehicles:
                vehicle = vehicles[model]
                print_vehicle_details(vehicle)
            else:
                print("Vehicle not found.")

        elif option == "7":
            # Display manufacturer details
            manufacturer_id = input("Enter manufacturer ID: ")
            if manufacturer_id in manufacturers:
                manufacturer = manufacturers[manufacturer_id]
                print(manufacturer.get_description())
                for vehicle in manufacturer.get_manufactured_vehicles():
                    print(f" - {vehicle.get_description()}")
            else:
                print("Manufacturer not found.")

        elif option == "8":
            # Exit
            break

        else:
            print("Invalid option. Please try again.")