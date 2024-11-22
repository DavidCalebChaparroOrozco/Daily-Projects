class BakeryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - Price: ${self.price:.2f}, Quantity: {self.quantity}"

    def total_value(self):
        return self.price * self.quantity