# Importing necessary libraries
from typing import List, Dict

# Class to represent a Product
class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    # Method to reduce stock when a product is added to the cart
    def reduce_stock(self, quantity: int):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False

    # Method to restock the product
    def restock(self, quantity: int):
        self.stock += quantity

# Class to represent a Shopping Cart
class ShoppingCart:
    def __init__(self):
        # Dictionary to hold products and their quantities
        self.items: Dict[Product, int] = {}  

    # Method to add a product to the cart
    def add_product(self, product: Product, quantity: int):
        if product.reduce_stock(quantity):
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            print(f"Added {quantity} of {product.name} to the cart.")
        else:
            print(f"Cannot add {quantity} of {product.name}. Not enough stock.")

    # Method to remove a product from the cart
    def remove_product(self, product: Product):
        if product in self.items:
            del self.items[product]
            print(f"Removed {product.name} from the cart.")
        else:
            print(f"{product.name} is not in the cart.")

    # Method to modify the quantity of a product in the cart
    def modify_product_quantity(self, product: Product, quantity: int):
        if product in self.items:
            current_quantity = self.items[product]
            if quantity <= current_quantity:
                # Restock removed items
                product.restock(current_quantity - quantity)  
                if quantity == 0:
                    self.remove_product(product)
                else:
                    self.items[product] = quantity
                    print(f"Updated {product.name} quantity to {quantity}.")
            else:
                print(f"Cannot increase {product.name} beyond available stock.")
        else:
            print(f"{product.name} is not in the cart.")

    # Method to calculate total price with tax and discounts
    def calculate_total(self, tax_rate: float = 0.0, discount: float = 0.0) -> float:
        subtotal = sum(product.price * quantity for product, quantity in self.items.items())
        total = subtotal + (subtotal * tax_rate) - discount
        return round(total, 2)

# Function to simulate testing of shopping cart operations
def run_tests():
    # Create some products
    apple = Product("Apple", 0.5, 10)
    banana = Product("Banana", 0.3, 5)
    
    # Create a shopping cart
    cart = ShoppingCart()

    # Test adding products

    # Should succeed
    cart.add_product(apple, 3)  
    # Should succeed
    cart.add_product(banana, 2)  

    # Test modifying product quantities

    # Should succeed (reducing)
    cart.modify_product_quantity(apple, 5)  
    # Should remove banana from cart
    cart.modify_product_quantity(banana, 0)  

    # Test removing a product that exists and one that does not exist
    # Should indicate banana is not in the cart
    cart.remove_product(banana)  

    # Test total calculation with tax and discount
    total_with_tax_and_discount = cart.calculate_total(tax_rate=0.1, discount=1.0)
    print(f"Total with tax and discount applied: ${total_with_tax_and_discount}")

# Main code execution for testing purposes
if __name__ == "__main__":
    run_tests()