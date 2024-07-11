# Represents a store that sells shirts.
class Store:

    # Initialize the store with a name, an empty list of shirts, and an empty list of customers.
    def __init__(self, name):
        """
        name: Name of the store
        """
        self.name = name
        self.shirts = []
        self.customers = []

    # Add a shirt to the store's inventory.
    def add_shirt(self, shirt):
        """
        shirt: Shirt object to be added
        """
        self.shirts.append(shirt)

    # Add a customer to the store.
    def add_customer(self, customer):
        """
        customer: Customer object to be added
        """
        self.customers.append(customer)

    # Sell a shirt to a customer.
    def sell_shirt(self, customer_name, shirt_name):
        """
        customer_name: Name of the customer
        shirt_name: Name of the shirt to be sold
        """
        customer = next((c for c in self.customers if c.name == customer_name), None)
        shirt = next((s for s in self.shirts if s.name == shirt_name), None)
        
        if customer and shirt:
            if shirt in customer.cart:
                customer.cart.remove(shirt)
                customer.purchased.append(shirt)
                self.shirts.remove(shirt)
                print(f"{shirt.name} has been sold to {customer.name}.")
            else:
                print(f"{shirt.name} is not in {customer.name}'s cart.")
        else:
            print("Customer or shirt not found.")

    # List all available shirts in the store.
    def list_shirts(self):
        if self.shirts:
            print("Available shirts:")
            for shirt in self.shirts:
                print(f"{shirt.name} - ${shirt.price}")
        else:
            print("No shirts available.")

    # List all customers of the store.
    def list_customers(self):
        if self.customers:
            print("Customers:")
            for customer in self.customers:
                print(customer.name)
        else:
            print("No customers found.")
