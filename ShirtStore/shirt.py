# Represents a shirt with a name, size, color, and price.
class Shirt:
    # Initialize a shirt with a name, size, color, and price.
    def __init__(self, name, size, color, price):
        """
        name: Name of the shirt
        size: Size of the shirt
        color: Color of the shirt
        price: Price of the shirt
        """
        self.name = name
        self.size = size
        self.color = color
        self.price = price

    # Return a string representation of the shirt.
    def __str__(self):
        """
        String describing the shirt
        """
        return f"{self.name} - Size: {self.size}, Color: {self.color}, Price: ${self.price}"
