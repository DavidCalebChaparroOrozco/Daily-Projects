class Plant:
    # Initialize a new plant with the provided attributes.
    def __init__(self, code, name, size, species, price):
        """
        code: Unique identifier for the plant
        name: Name of the plant
        size: Size of the plant in meters
        species: Species of the plant
        price: Price of the plant
        """
        self.code = code
        self.name = name
        self.size = size
        self.species = species
        self.price = price

class Nursery:
    # Initialize the nursery with an empty list of plants.
    def __init__(self):
        self.plants = []

    # Add a new plant to the nursery.
    def add_plant(self, plant):
        """
        plant: The plant object to be added
        """
        self.plants.append(plant)

    # Create a sublist of plants that are taller than 2 meters.
    def get_tall_plants(self):
        """
        List of plants taller than 2 meters
        """
        return [plant for plant in self.plants if plant.size > 2]

    # Remove all plants with the given name from the nursery.
    def remove_plant_by_name(self, name):
        """
        name: Name of the plants to be removed
        """
        self.plants = [plant for plant in self.plants if plant.name != name]

    # Count the number of plants of a specific species.
    def count_plants_by_species(self, species):
        """
        species: Species to count
        Number of plants of the given species
        """
        return sum(1 for plant in self.plants if plant.species == species)

# Example usage
if __name__ == "__main__":
    # Initialize the nursery
    nursery = Nursery()

    # Create and add plants to the nursery
    nursery.add_plant(Plant("001", "Rose", 1.5, "Flowering", 10.99))
    nursery.add_plant(Plant("002", "Oak", 3.0, "Tree", 20.50))
    nursery.add_plant(Plant("003", "Maple", 2.5, "Tree", 25.00))
    nursery.add_plant(Plant("004", "Cactus", 0.8, "Succulent", 15.75))
    nursery.add_plant(Plant("005", "Sunflower", 3.2, "Flowering", 12.99))
    nursery.add_plant(Plant("006", "Pine", 4.0, "Tree", 30.00))

    # Get and print all plants taller than 2 meters
    tall_plants = nursery.get_tall_plants()
    print("Plants taller than 2 meters:")
    for plant in tall_plants:
        print(f"Name: {plant.name}, Size: {plant.size}m")

    # Remove all plants with the name "Cactus"
    nursery.remove_plant_by_name("Cactus")
    print("\nRemaining plants after removing 'Cactus':")
    for plant in nursery.plants:
        print(f"Name: {plant.name}, Species: {plant.species}")

    # Count and print the number of plants of the species "Tree"
    tree_count = nursery.count_plants_by_species("Tree")
    print(f"\nNumber of 'Tree' species plants: {tree_count}")
