# Importing necessary libraries
import json

# Function to load data from JSON file
def load_customers():
    with open("data.json", "r", encoding="utf-8") as file:
        customers = json.load(file)
    return customers

# Function to save data to JSON file
def save_customers(customers):
    with open("data.json", "w") as file:
        json.dump(customers, file, indent=4)

# Feature to show main menu
def main_menu():
    print(" Customer Management System ".center(50,"*"))
    print("1. Show all customers")
    print("2. Search customer by name")
    print("3. Update customer information")
    print("4. Delete client")
    print("5. Add new client")
    print("6. Exit")

# data info:
# "id": 1,
# "first_name": "Melessa",
# "last_name": "Bodham",
# "email": "mbodham0@ebay.co.uk",
# "gender": "Female",
# "product": "Bag - Bread, White, Plain",
# "quantity": 1,
# "city": "Sîngerei",
# "address": "193 Shoshone Place",
# "price": "$2.66"

# Feature to show all customers
def show_customers(customers):
    print("\n Client List: ")
    for customer in customers:
        print(f"ID: {customer['id']}, " +
            f"Name: {customer['first_name']} {customer['last_name']}, " +
            f"Email: {customer['email']}, " +
            f"Genre: {customer['gender']}, " +
            f"Product: {customer['product']}, " +
            f"Quantity: {customer['quantity']}, " +
            f"City: {customer['city']}, " +
            f"Address: {customer['address']}, " +
            f"Prices: {customer['price']}")


# Feature to search for a customer by name
def search_customer_name(customers):
    name = input("Enter the name of the client to search:")
    found = []

    for customer in customers:
        if name.lower() in customer['first_name'].lower() or name.lower() in customer['last_name'].lower():
            found.append(customer)
    
    if found:
        print("\n Customers Founds")
        for customer in found:
            print(f"ID: {customer['id']}, Nombre: {customer['first_name']} {customer['last_name']}, Email: {customer['email']}, Ciudad: {customer['city']}")
    else:
        print("No clients were found with that name.")

# Function to update a customer's information
def update_customer(customers):
    id_customer = input("Enter the ID of the client you want to update: ")

    while not id_customer.isdigit():
        print("Please enter a valid ID (numeric value).")
        id_customer = input("Enter the ID of the client you want to update: ")
    id_customer = int(id_customer)

    for customer in customers:
        if customer["id"] == id_customer:
            print(f"\nUpdating customer information: {customer['first_name']} {customer['last_name']}")
            customer['first_name'] = input("New name: ")
            customer['last_name'] = input("New last name: ")
            customer['email'] = input("New email: ")
            customer['city'] = input("New city: ")
            print("Customer information updated.")
            return
    print("No client with that ID was found.")

# Function to delete a customer
def delete_client(customers):
    customer_id = int(input("Enter the ID of the customer you want to delete: "))
    for client in customers:
        if client['id'] == customer_id:
            confirmation = input(f"Are you sure you want to delete customer {client['first_name']} {client['last_name']}? (y/n): ")
            if confirmation.lower() == 'y':
                customers.remove(client)
                print("Client deleted successfully.")
            return
    print("No client with that ID was found.")


# Function to add a new customer
def add_new_customer(customers):
    new_customer = {}
    new_customer['id'] = len(customers) + 1
    new_customer['first_name'] = input("Enter the first name of the new client: ")
    new_customer['last_name'] = input("Enter the last name of the new client: ")
    new_customer['email'] = input("Enter the email of the new client: ")
    new_customer['gender'] = input("Enter the gender of the new client: ")
    new_customer['product'] = input("Enter the product bought by the new client: ")
    new_customer['quantity'] = int(input("Enter the quantity of the product bought by the new client: "))
    new_customer['city'] = input("Enter the city of the new client: ")
    new_customer['address'] = input("Enter the address of the new client: ")
    new_customer_price = input("Enter the price paid by the new client: ")
    new_customer['price'] = f"${new_customer_price}"

    customers.append(new_customer)
    print("New client added successfully.")

def main():
    customers = load_customers()
    while True:
        main_menu()
        option = input("\nSelect an option: ")
        if option == '1':
            show_customers(customers)
        elif option == '2':
            search_customer_name(customers)
        elif option == '3':
            update_customer(customers)
            save_customers(customers)
        elif option == '4':
            delete_client(customers)
            save_customers(customers)
        elif option == '5':
            add_new_customer(customers)
            save_customers(customers)
        elif option == '6':
            print("See you soon!")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()