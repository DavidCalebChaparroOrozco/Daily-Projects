# Importing necessary libraries
from abc import ABC, abstractmethod

# Base class for Person (Customer and Staff)
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

    # Getter method to retrieve the name of the person
    def get_name(self):
        return self._name

    # Getter method to retrieve the ID number of the person
    def get_id_number(self):
        return self._id_number


# Class for Customer
class Customer(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._order = []

    # Implement the abstract method to get the description of the customer
    def get_description(self):
        return f"Customer: {self.get_name()} (ID: {self.get_id_number()})"

    # Method to add an item to the customer's order
    def add_to_order(self, item):
        self._order.append(item)

    # Method to get the order details
    def get_order(self):
        return self._order


# Class for Staff (Server or Cashier)
class Staff(Person):
    def __init__(self, name, id_number, position):
        super().__init__(name, id_number)
        self._position = position

    # Implement the abstract method to get the description of the staff
    def get_description(self):
        return f"{self._position}: {self.get_name()} (ID: {self.get_id_number()})"


# Class for Menu Item (Food or Drink)
class MenuItem:
    def __init__(self, name, category, price):
        self._name = name
        self._category = category  # Food or Drink
        self._price = price

    # Method to get the description of the menu item
    def get_description(self):
        return f"{self._name} ({self._category}) - ${self._price:.2f}"

    # Method to get the price of the menu item
    def get_price(self):
        return self._price


# Function to calculate the total bill and tips
def calculate_bill(customer, tip_percentage, server):
    total = sum(item.get_price() for item in customer.get_order())
    tip = total * (tip_percentage / 100)
    grand_total = total + tip

    print(f"\nBill for {customer.get_name()} (ID: {customer.get_id_number()}):")
    print("Ordered items:")
    for item in customer.get_order():
        print(f" - {item.get_description()}")

    print(f"\nTotal: ${total:.2f}")
    print(f"Tip ({tip_percentage}%): ${tip:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")
    print(f"Served by: {server.get_name()}\n")


# Function to display the menu
def display_menu():
    print("\nRestaurant Ordering System")
    print("1. Add item to order")
    print("2. Display customer details")
    print("3. Generate bill")
    print("4. Exit")
    print("=".center(50, "="))
    return input("Select an option: ")


# Main code
if __name__ == "__main__":
    # Create instances of staff members
    server1 = Staff("Emily Johnson", "S001", "Server")
    cashier1 = Staff("Michael Thompson", "C001", "Cashier")

    # Create instances of menu items
    item1 = MenuItem("Pasta Carbonara", "Food", 12.99)
    item2 = MenuItem("Cheeseburger", "Food", 9.99)
    item3 = MenuItem("Coke", "Drink", 1.99)
    item4 = MenuItem("Wine", "Drink", 6.99)

    # Dictionary to hold customers
    customers = {}

    while True:
        option = display_menu()

        if option == "1":
            # Add item to order
            customer_name = input("Enter customer name: ")
            customer_id = input("Enter customer ID: ")

            if customer_id not in customers:
                customers[customer_id] = Customer(customer_name, customer_id)

            customer = customers[customer_id]

            print("\nMenu:")
            print(f"1. {item1.get_description()}")
            print(f"2. {item2.get_description()}")
            print(f"3. {item3.get_description()}")
            print(f"4. {item4.get_description()}")

            item_choice = input("Select item to add (1-4): ")

            if item_choice == "1":
                customer.add_to_order(item1)
            elif item_choice == "2":
                customer.add_to_order(item2)
            elif item_choice == "3":
                customer.add_to_order(item3)
            elif item_choice == "4":
                customer.add_to_order(item4)
            else:
                print("Invalid option.")
            print("Item added to order.")

        elif option == "2":
            # Display customer details
            customer_id = input("Enter customer ID: ")
            if customer_id in customers:
                customer = customers[customer_id]
                print(customer.get_description())
                print("Order:")
                for item in customer.get_order():
                    print(f" - {item.get_description()}")
            else:
                print("Customer not found.")

        elif option == "3":
            # Generate bill
            customer_id = input("Enter customer ID: ")
            if customer_id in customers:
                customer = customers[customer_id]
                tip_percentage = float(input("Enter tip percentage: "))
                calculate_bill(customer, tip_percentage, server1)
            else:
                print("Customer not found.")

        elif option == "4":
            # Exit
            print("Thank you for using the Restaurant Ordering System.")
            break

        else:
            print("Invalid option. Please try again.")
