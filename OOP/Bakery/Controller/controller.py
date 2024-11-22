from Model.model import BakeryItem

class BakeryController:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        new_item = BakeryItem(name, price, quantity)
        self.items.append(new_item)
        return f"{name} has been added to the bakery."

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            removed_item = self.items.pop(index)
            return f"{removed_item.name} has been removed from the bakery."
        else:
            return "Error: Invalid index."

    def update_item(self, index, new_name=None, new_price=None, new_quantity=None):
        if 0 <= index < len(self.items):
            if new_name:
                self.items[index].name = new_name
            if new_price is not None:
                self.items[index].price = new_price
            if new_quantity is not None:
                self.items[index].quantity = new_quantity
            
            return f"{self.items[index].name} has been updated."
        
        return "Error: Invalid index."

    def search_item_by_name(self, name):
        found_items = [item for item in self.items if name.lower() in item.name.lower()]
        
        if found_items:
            return found_items
        else:
            return None

    def get_all_items(self):
        return self.items
    
    def total_inventory_value(self):
        return sum(item.total_value() for item in self.items)