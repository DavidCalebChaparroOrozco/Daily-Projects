from store import Store
from shirt import Shirt
from customer import Customer

# Main function to run the shirt store application.
def main():

    # Create a store
    store = Store("The Shirt Shop")

    # Add some initial shirts to the store
    store.add_shirt(Shirt("Classic White Tee", "M", "White", 20))
    store.add_shirt(Shirt("Sporty Red Shirt", "L", "Red", 25))
    store.add_shirt(Shirt("Elegant Black Shirt", "S", "Black", 30))

    # Print the menu options for the user.
    def print_menu():
        print("\nThe Shirt Shop Menu")
        print("1. List available shirts")
        print("2. Add a new shirt")
        print("3. List customers")
        print("4. Add a new customer")
        print("5. Add shirt to customer's cart")
        print("6. View customer's cart")
        print("7. Sell shirt to customer")
        print("8. View customer's purchased shirts")
        print("9. Exit")
        print("=".center(50, "="))

    while True:
        # Display the menu and get the user's choice
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # List all available shirts in the store
            store.list_shirts()
        elif choice == '2':
            # Add a new shirt to the store
            name = input("Enter shirt name: ")
            size = input("Enter shirt size: ")
            color = input("Enter shirt color: ")
            price = float(input("Enter shirt price: "))
            store.add_shirt(Shirt(name, size, color, price))
            print("Shirt added successfully.")
        elif choice == '3':
            # List all customers of the store
            store.list_customers()
        elif choice == '4':
            # Add a new customer to the store
            name = input("Enter customer name: ")
            store.add_customer(Customer(name))
            print("Customer added successfully.")
        elif choice == '5':
            # Add a shirt to a customer's cart
            customer_name = input("Enter customer name: ")
            shirt_name = input("Enter shirt name: ")
            customer = next((c for c in store.customers if c.name == customer_name), None)
            shirt = next((s for s in store.shirts if s.name == shirt_name), None)
            if customer and shirt:
                customer.add_to_cart(shirt)
            else:
                print("Customer or shirt not found.")
        elif choice == '6':
            # View the contents of a customer's cart
            customer_name = input("Enter customer name: ")
            customer = next((c for c in store.customers if c.name == customer_name), None)
            if customer:
                customer.view_cart()
            else:
                print("Customer not found.")
        elif choice == '7':
            # Sell a shirt to a customer
            customer_name = input("Enter customer name: ")
            shirt_name = input("Enter shirt name: ")
            store.sell_shirt(customer_name, shirt_name)
        elif choice == '8':
            # View the shirts purchased by a customer
            customer_name = input("Enter customer name: ")
            customer = next((c for c in store.customers if c.name == customer_name), None)
            if customer:
                customer.view_purchased()
            else:
                print("Customer not found.")
        elif choice == '9':
            # Exit the program
            print("Exiting the program. Goodbye!")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
