# Represents a customer who can add shirts to their cart and purchase them.
class Customer:

    # Initialize a customer with a name, an empty cart, and an empty list of purchased shirts.
    def __init__(self, name):
        """
        name: Name of the customer
        """
        self.name = name
        self.cart = []
        self.purchased = []

    # Add a shirt to the customer's cart.
    def add_to_cart(self, shirt):
        """
        shirt: Shirt object to be added to the cart
        """
        self.cart.append(shirt)
        print(f"{shirt.name} added to {self.name}'s cart.")

    # View all shirts in the customer's cart.
    def view_cart(self):
        if self.cart:
            print(f"{self.name}'s cart:")
            for shirt in self.cart:
                print(shirt)
        else:
            print(f"{self.name}'s cart is empty.")

    # View all shirts purchased by the customer.
    def view_purchased(self):
        if self.purchased:
            print(f"{self.name}'s purchased shirts:")
            for shirt in self.purchased:
                print(shirt)
        else:
            print(f"{self.name} has not purchased any shirts yet.")
