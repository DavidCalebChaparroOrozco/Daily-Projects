# Importing necessary libraries
from abc import ABC, abstractmethod

# Abstraction and Encapsulation (Base Class for Ice Cream)
class IceCream(ABC):
    def __init__(self, flavor, price):
        # Encapsulation: Making attributes private
        self._flavor = flavor  
        self._price = price    

    @abstractmethod
    def get_description(self):
        """
        Abstract method to get the description of the ice cream.
        Subclasses must implement this method.
        """
        pass

    # Getter method to retrieve the flavor of the ice cream.
    def get_flavor(self):
        return self._flavor

    # Getter method to retrieve the price of the ice cream.
    def get_price(self):
        return self._price


# Inheritance
class ScoopIceCream(IceCream):
    def __init__(self, flavor, price, scoops):
        super().__init__(flavor, price)
        self._scoops = scoops

    # Implement the abstract method to get the description of the scoop ice cream.
    def get_description(self):
        return f"{self._scoops} scoops of {self.get_flavor()} ice cream"

    # Calculate the total price of the scoop ice cream.
    def get_total_price(self):
        return self._price * self._scoops


# Inheritance
class Sundae(IceCream):
    def __init__(self, flavor, price, toppings):
        super().__init__(flavor, price)
        self._toppings = toppings

    # Implement the abstract method to get the description of the sundae.
    def get_description(self):
        toppings_str = ", ".join(self._toppings)
        return f"{self.get_flavor()} sundae with {toppings_str}"

    # Calculate the total price of the sundae.
    def get_total_price(self):
        return self._price + 0.5 * len(self._toppings)


# Polymorphism (Function to print ice cream details)
def print_ice_cream_details(ice_cream):
    # Print the description and total price of the given ice cream.
    print(ice_cream.get_description())
    print(f"Total price: ${ice_cream.get_total_price():.2f}")


# Cohesion: Each class has a single responsibility and methods related to that responsibility.
# Coupling: The classes are loosely coupled. Changes in one class minimally affect others.

if __name__ == "__main__":
    # Create instances of ice cream
    vanilla_scoop = ScoopIceCream("vanilla", 2.0, 3)
    chocolate_sundae = Sundae("chocolate", 4.0, ["sprinkles", "cherry", "whipped cream"])

    # Print the details of the ice cream
    print_ice_cream_details(vanilla_scoop)
    print_ice_cream_details(chocolate_sundae)

    # Example 3: Strawberry ice cream with 2 scoops
    strawberry_scoop = ScoopIceCream("strawberry", 2.5, 2)
    print_ice_cream_details(strawberry_scoop)

    # Example 4: Mint Sundae with Chocolate Chips and Whipped Cream
    mint_sundae = Sundae("mint", 4.5, ["chocolate chips", "whipped cream"])
    print_ice_cream_details(mint_sundae)

    # Example 5: Chocolate ice cream with 4 scoops
    chocolate_scoop = ScoopIceCream("chocolate", 3.0, 4)
    print_ice_cream_details(chocolate_scoop)