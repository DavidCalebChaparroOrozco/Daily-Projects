class House:
    def __init__(self, id, address, rent, bedrooms, bathrooms, available):
        self.id = id
        self.address = address
        self.rent = rent
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.available = available

    def __str__(self):
        return f"ID: {self.id}, Address: {self.address}, Rent: ${self.rent}, Bedrooms: {self.bedrooms}, Bathrooms: {self.bathrooms}, Available: {'Yes' if self.available else 'No'}"


class HouseModel:
    def __init__(self):
        self.houses = []
        self.current_id = 1

    def add_house(self, address, rent, bedrooms, bathrooms):
        house = House(self.current_id, address, rent, bedrooms, bathrooms, True)
        self.houses.append(house)
        self.current_id += 1

    def remove_house(self, house_id):
        for house in self.houses:
            if house.id == house_id:
                self.houses.remove(house)
                return True
        return False

    def get_all_houses(self):
        return self.houses

    def get_available_houses(self):
        return [house for house in self.houses if house.available]