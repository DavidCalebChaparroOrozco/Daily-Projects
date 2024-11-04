class CandyInventory:
    def __init__(self):
        # Initialize an empty dictionary to store candy types and their quantities
        self.inventory = {}

    # Add a specified quantity of candy to the inventory.
    def add_candy(self, candy_name, quantity):
        """        
        candy_name: Name of the candy to add
        quantity: Quantity of the candy to add
        """
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
        
        # If the candy already exists, update its quantity
        if candy_name in self.inventory:
            self.inventory[candy_name] += quantity
        else:
            self.inventory[candy_name] = quantity
        
        print(f"Added {quantity} {candy_name}(s) to inventory.")
    
    # Remove a specified quantity of candy from the inventory recursively.
    def remove_candy(self, candy_name, quantity):
        """
        candy_name: Name of the candy to remove
        quantity: Quantity of the candy to remove
        """
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
        
        # Check if the candy exists in inventory
        if candy_name not in self.inventory:
            print(f"{candy_name} is not in inventory.")
            return
        
        # If there is enough candy to remove
        if self.inventory[candy_name] >= quantity:
            self.inventory[candy_name] -= quantity
            print(f"Removed {quantity} {candy_name}(s) from inventory.")
            # If the quantity reaches zero, delete the entry from inventory
            if self.inventory[candy_name] == 0:
                del self.inventory[candy_name]
                print(f"{candy_name} is now out of stock.")
        else:
            print(f"Not enough {candy_name} in inventory. Current stock: {self.inventory[candy_name]}")
    
    # Display all candies in the inventory.
    def display_inventory(self):
        if not self.inventory:
            print("The inventory is empty.")
            return
        
        print("Current Candy Inventory:")
        for candy, quantity in self.inventory.items():
            print(f"{candy}: {quantity}")

# Example usage
if __name__ == "__main__":
    # Create an instance of CandyInventory
    my_inventory = CandyInventory()
    
    # Adding candies to the inventory
    my_inventory.add_candy("Chocolate", 10)
    my_inventory.add_candy("Gummy Bears", 5)
    
    # Display current inventory
    my_inventory.display_inventory()
    
    # Removing candies from the inventory
    my_inventory.remove_candy("Chocolate", 3)
    # Attempting to remove more than available
    my_inventory.remove_candy("Gummy Bears", 6)  
    
    # Display updated inventory
    my_inventory.display_inventory()