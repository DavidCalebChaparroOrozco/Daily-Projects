from model.model import Box, BoxInventory
from view.view import BoxView
import json

# Manages interactions between Model and View
class BoxController:
    def __init__(self):
        self.inventory = BoxInventory()

    # Main application loop
    def run(self):
        while True:
            BoxView.display_menu()
            choice = input("Select an option: ")

            if choice == '1':
                self.view_all_boxes()
            elif choice == '2':
                self.add_new_box()
            elif choice == '3':
                self.remove_box()
            elif choice == '4':
                self.update_box()
            elif choice == '5':
                self.search_box()
            elif choice == '6':
                self.calculate_total_value()
            elif choice == '7':
                self.filter_by_material()
            elif choice == '8':
                self.sort_boxes_by_price()
            elif choice == '9':
                self.export_report()
            elif choice == '0':
                break
            else:
                BoxView.display_message("Invalid option!")

    # Display all boxes in inventory
    def view_all_boxes(self):
        boxes = self.inventory.get_all_boxes()
        BoxView.display_boxes(boxes)

    # Add a new box to inventory
    def add_new_box(self):
        details = BoxView.get_box_input()
        new_box = Box(*details)
        self.inventory.add_box(new_box)
        BoxView.display_message("Box added successfully!")

    
    # Remove a box from inventory
    def remove_box(self):
        box_id = input("Enter Box ID to remove: ")
        box = self.inventory.find_box_by_id(box_id)
        
        if box:
            self.inventory.remove_box(box_id)
            BoxView.display_message(f"Box {box_id} removed successfully!")
        else:
            BoxView.display_message(f"Box {box_id} not found!")

    # Update existing box details
    def update_box(self):
        box_id = input("Enter Box ID to update: ")
        existing_box = self.inventory.find_box_by_id(box_id)
        
        if existing_box:
            # Collect new details
            new_details = BoxView.get_box_input()
            updated_box = Box(*new_details)
            
            if self.inventory.update_box(box_id, updated_box):
                BoxView.display_message(f"Box {box_id} updated successfully!")
            else:
                BoxView.display_message("Update failed!")
        else:
            BoxView.display_message(f"Box {box_id} not found!")

    # Search for a box by ID
    def search_box(self):
        box_id = input("Enter Box ID to search: ")
        box = self.inventory.find_box_by_id(box_id)
        
        if box:
            BoxView.display_boxes([box])
        else:
            BoxView.display_message(f"Box {box_id} not found!")

    # Calculate total inventory value
    def calculate_total_value(self):
        total_value = sum(box.price for box in self.inventory.get_all_boxes())
        BoxView.display_message(f"Total Inventory Value: ${total_value:.2f}")

    # Filter boxes by material
    def filter_by_material(self):
        material = input("Enter material to filter: ").lower()
        filtered_boxes = [
            box for box in self.inventory.get_all_boxes() 
            if box.material.lower() == material
        ]
        
        if filtered_boxes:
            BoxView.display_boxes(filtered_boxes)
        else:
            BoxView.display_message(f"No boxes found with material: {material}")

    # Sort boxes by price
    def sort_boxes_by_price(self):
        sorted_boxes = sorted(
            self.inventory.get_all_boxes(), 
            key=lambda x: x.price
        )
        BoxView.display_boxes(sorted_boxes)

    # Export inventory report to a text file
    def export_report(self):
        try:
            with open("inventory_report.txt", "w") as file:
                file.write("Box Inventory Report\n")
                file.write("=" * 50 + "\n")
                
                for box in self.inventory.get_all_boxes():
                    file.write(f"ID: {box.id}\n")
                    file.write(f"Name: {box.name}\n")
                    file.write(f"Material: {box.material}\n")
                    file.write(f"Dimensions: {box.dimensions}\n")
                    file.write(f"Weight: {box.weight} kg\n")
                    file.write(f"Price: ${box.price:.2f}\n")
                    file.write("-" * 50 + "\n")
            
            BoxView.display_message("Inventory report exported successfully!")
        except Exception as e:
            BoxView.display_message(f"Error exporting report: {e}")

    # Load some initial box data for testing
    def load_initial_data(self):
        initial_boxes = [
            Box("001", "Storage Box", "Cardboard", "30x20x15", 0.5, 5.99),
            Box("002", "Shipping Container", "Metal", "200x100x100", 50.0, 299.99),
            Box("003", "Jewelry Box", "Wood", "15x10x8", 0.3, 49.99),
            Box("004", "Electronics Box", "Plastic", "40x30x25", 1.2, 24.50)
        ]
        
        for box in initial_boxes:
            self.inventory.add_box(box)


    # Save inventory to a JSON file
    def save_inventory(self):
        data = [{
            'id': box.id,
            'name': box.name,
            'material': box.material,
            'dimensions': box.dimensions,
            'weight': box.weight,
            'price': box.price
        } for box in self.inventory.get_all_boxes()]
        
        with open('inventory.json', 'w') as f:
            json.dump(data, f, indent=4)

    # Load inventory from JSON file
    def load_inventory(self):
        try:
            with open('inventory.json', 'r') as f:
                data = json.load(f)
                for item in data:
                    box = Box(
                        item['id'], 
                        item['name'], 
                        item['material'], 
                        item['dimensions'], 
                        item['weight'], 
                        item['price']
                        )
                    self.inventory.add_box(box)
        except FileNotFoundError:
            print("No previous inventory found.")