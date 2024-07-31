# Importing necessary libraries
from abc import ABC, abstractmethod
import unittest

# Base Class for Person (Customer and Staff)
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


# Inheritance for Customer
class Customer(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._pets = []

    # Implement the abstract method to get the description of the customer.
    def get_description(self):
        return f"Customer: {self.get_name()} (ID: {self.get_id_number()})"

    # Method to adopt a pet.
    def adopt_pet(self, pet):
        self._pets.append(pet)

    # Method to get the list of pets the customer has adopted.
    def get_pets(self):
        return self._pets


# Inheritance for Staff
class Staff(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._assigned_pets = []

    # Implement the abstract method to get the description of the staff.
    def get_description(self):
        return f"Staff: {self.get_name()} (ID: {self.get_id_number()})"

    # Method to assign a pet to the staff.
    def assign_pet(self, pet):
        self._assigned_pets.append(pet)

    # Method to get the list of pets the staff is responsible for.
    def get_assigned_pets(self):
        return self._assigned_pets


# Class for Pet
class Pet:
    def __init__(self, name, breed, age, price):
        self._name = name
        self._breed = breed
        self._age = age
        self._price = price

    # Method to get the description of the pet.
    def get_description(self):
        return f"Pet: {self._name}, Breed: {self._breed}, Age: {self._age}, Price: ${self._price:.2f}"


# Function to display the menu
def display_menu():
    print("\nPet Store Management System")
    print("1. Adopt a pet")
    print("2. Display customer details")
    print("3. Display pet details")
    print("4. Exit")
    print("=".center(50, "="))
    return input("Select an option: ")


# Main code
if __name__ == "__main__":
    # Create instances of staff
    staff1 = Staff("Alice", "S001")
    staff2 = Staff("Bob", "S002")

    # Create instances of pets
    pet1 = Pet("Buddy", "Golden Retriever", 2, 500.00)
    pet2 = Pet("Mittens", "Siamese Cat", 3, 300.00)

    # Assign pets to staff
    staff1.assign_pet(pet1)
    staff2.assign_pet(pet2)

    # Dictionary to hold customers
    customers = {}

    while True:
        option = display_menu()

        if option == "1":
            # Adopt a pet
            customer_name = input("Enter customer name: ")
            customer_id = input("Enter customer ID: ")
            pet_name = input("Enter pet name (Buddy/Mittens): ")

            if customer_id not in customers:
                customers[customer_id] = Customer(customer_name, customer_id)

            customer = customers[customer_id]

            if pet_name == "Buddy":
                pet = pet1
            elif pet_name == "Mittens":
                pet = pet2
            else:
                print("Invalid pet name.")
                continue

            customer.adopt_pet(pet)
            print("Pet adopted successfully.")

        elif option == "2":
            # Display customer details
            customer_id = input("Enter customer ID: ")
            if customer_id in customers:
                customer = customers[customer_id]
                print(customer.get_description())
                for pet in customer.get_pets():
                    print(f" - {pet.get_description()}")
            else:
                print("Customer not found.")

        elif option == "3":
            # Display pet details
            pet_name = input("Enter pet name (Buddy/Mittens): ")

            if pet_name == "Buddy":
                print(pet1.get_description())
            elif pet_name == "Mittens":
                print(pet2.get_description())
            else:
                print("Invalid pet name.")

        elif option == "4":
            # Exit
            break

        else:
            print("Invalid option. Please try again.")

# Unit Tests
class TestPetStore(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John Doe", "C001")
        self.staff = Staff("Jane Doe", "S001")
        self.pet = Pet("Rex", "Bulldog", 5, 400.00)

    def test_customer_adoption(self):
        self.customer.adopt_pet(self.pet)
        self.assertIn(self.pet, self.customer.get_pets())

    def test_staff_assignment(self):
        self.staff.assign_pet(self.pet)
        self.assertIn(self.pet, self.staff.get_assigned_pets())

    def test_pet_description(self):
        description = self.pet.get_description()
        self.assertEqual(description, "Pet: Rex, Breed: Bulldog, Age: 5, Price: $400.00")

    def test_customer_description(self):
        description = self.customer.get_description()
        self.assertEqual(description, "Customer: John Doe (ID: C001)")

    def test_staff_description(self):
        description = self.staff.get_description()
        self.assertEqual(description, "Staff: Jane Doe (ID: S001)")

if __name__ == "__main__":
    unittest.main()
