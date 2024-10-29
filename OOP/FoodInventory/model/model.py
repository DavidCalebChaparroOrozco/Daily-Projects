import csv
from datetime import datetime

class FoodItem:
    def __init__(self, name, category, quantity, price, expiration_date):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d").date() if expiration_date else None

    def is_expired(self):
        return datetime.now().date() > self.expiration_date if self.expiration_date else False

    def days_until_expired(self):
        if not self.expiration_date:
            return None
        return (self.expiration_date - datetime.now().date()).days

class InventoryHistory:
    def __init__(self):
        self.history = []

    def log_change(self, action, item_name, quantity):
        change = {
            "action": action,
            "item_name": item_name,
            "quantity": quantity,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.history.append(change)

    def get_history(self):
        return self.history

class Inventory:
    def __init__(self):
        self.food_items = []
        self.history = InventoryHistory()

    def add_item(self, food_item):
        self.food_items.append(food_item)
        self.history.log_change("add", food_item.name, food_item.quantity)

    def remove_item(self, item_name):
        for item in self.food_items:
            if item.name.lower() == item_name.lower():
                self.history.log_change("remove", item.name, item.quantity)
                self.food_items.remove(item)
                return True
        return False

    def get_near_expiration_items(self):
        return [item for item in self.food_items if item.days_until_expired() is not None and 0 < item.days_until_expired() <= 7]

    def get_total_value(self):
        return sum(item.price * item.quantity for item in self.food_items)

    def search_items(self, keyword, category=None):
        results = [item for item in self.food_items if keyword.lower() in item.name.lower()]
        if category:
            results = [item for item in results if item.category.lower() == category.lower()]
        return results

    def import_data(self, filename):
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    quantity = int(row["quantity"]) if row["quantity"] else 0
                    price = float(row["price"]) if row["price"] else 0.0
                    
                    expiration_date_str = row["expiration_date"]
                    expiration_date = expiration_date_str if expiration_date_str else None
                    
                    food_item = FoodItem(row["name"], row["category"], quantity, price, expiration_date)
                    self.add_item(food_item)  # Use add_item to log history
            print("Data imported successfully.")
        except Exception as e:
            print(f"An error occurred while importing data: {e}")

    def export_data(self, filename):
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "category", "quantity", "price", "expiration_date"])
            writer.writeheader()
            for item in self.food_items:
                writer.writerow({"name": item.name,
                                "category": item.category,
                                "quantity": item.quantity,
                                "price": item.price,
                                "expiration_date": item.expiration_date.strftime("%Y-%m-%d") if item.expiration_date else ""})