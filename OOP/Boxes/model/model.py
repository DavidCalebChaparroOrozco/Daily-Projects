# Represents a box with its properties and methods
class Box:
    def __init__(self, id, name, material, dimensions, weight, price):
        self.id = id
        self.name = name
        self.material = material
        self.dimensions = dimensions
        self.weight = weight
        self.price = price

# Manages the collection of boxes
class BoxInventory:
    def __init__(self):
        self.boxes = []

    # Add a new box to inventory
    def add_box(self, box):
        self.boxes.append(box)
        return True

    # Remove a box from inventory by ID
    def remove_box(self, box_id):
        self.boxes = [box for box in self.boxes if box.id != box_id]
        return True

    # Retrieve all boxes
    def get_all_boxes(self):
        return self.boxes

    # Find a box by its ID
    def find_box_by_id(self, box_id):
        return next((box for box in self.boxes if box.id == box_id), None)

    # Update an existing box
    def update_box(self, box_id, updated_box):
        for index, box in enumerate(self.boxes):
            if box.id == box_id:
                self.boxes[index] = updated_box
                return True
        return False
