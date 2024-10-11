class Cellphone:
    def __init__(self, model_name, brand, stock):
        # Constructor to initialize a cellphone object
        self.model_name = model_name
        self.brand = brand
        self.stock = stock

    def get_model_name(self):
        # Returns the name of the cellphone model
        return self.model_name

    def get_brand(self):
        # Returns the brand of the cellphone
        return self.brand

    def get_stock(self):
        # Returns the available stock for the cellphone model
        return self.stock

    def update_stock(self, new_stock):
        # Updates the stock level of the cellphone model
        self.stock = new_stock

class Inventory:
    def __init__(self):
        # Constructor initializes an empty inventory
        self.cellphones = []

    def add_cellphone(self, cellphone):
        # Adds a new cellphone model to the inventory
        self.cellphones.append(cellphone)

    def find_cellphone(self, model_name):
        # Searches for a cellphone by its model name in the inventory
        for phone in self.cellphones:
            if phone.get_model_name().lower() == model_name.lower():
                return phone
        return None

    def get_inventory(self):
        # Returns the list of all cellphones in the inventory
        return self.cellphones
