class Lotion:
    def __init__(self, lotion_id, name, brand, price, stock):
        self.lotion_id = lotion_id
        self.name = name
        self.brand = brand
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.lotion_id}: {self.name} by {self.brand}, Price: ${self.price}, Stock: {self.stock}"

class LotionModel:
    def __init__(self):
        self.lotions = []

    def add_lotion(self, lotion):
        self.lotions.append(lotion)

    def remove_lotion(self, lotion_id):
        for lotion in self.lotions:
            if lotion.lotion_id == lotion_id:
                self.lotions.remove(lotion)
                return True
        return False

    def get_all_lotions(self):
        return self.lotions

    def find_lotion_by_id(self, lotion_id):
        for lotion in self.lotions:
            if lotion.lotion_id == lotion_id:
                return lotion
        return None