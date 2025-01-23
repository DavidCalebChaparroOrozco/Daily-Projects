# Handles user interface and interactions
class BoxView:
    # Display main menu options
    @staticmethod
    def display_menu():
        print("\n🔲 Box Management System by David Caleb🔲")
        print("1. View All Boxes")
        print("2. Add New Box")
        print("3. Remove Box")
        print("4. Update Box Details")
        print("5. Search Box by ID")
        print("6. Calculate Total Inventory Value")
        print("7. Filter Boxes by Material")
        print("8. Sort Boxes by Price")
        print("9. Export Inventory Report")
        print("0. Exit System")

    @staticmethod
    # Collect box details from user
    def get_box_input():
        id = input("Enter Box ID: ")
        name = input("Enter Box Name: ")
        material = input("Enter Box Material: ")
        dimensions = input("Enter Box Dimensions (L x W x H): ")
        weight = float(input("Enter Box Weight (kg): "))
        price = float(input("Enter Box Price: "))
        return id, name, material, dimensions, weight, price

    @staticmethod
    # Display list of boxes
    def display_boxes(boxes):
        if not boxes:
            print("No boxes found!")
            return
        
        print("\n{:<10} {:<15} {:<15} {:<20} {:<10} {:<10}".format(
            "ID", "Name", "Material", "Dimensions", "Weight", "Price"))
        print("-" * 80)
        
        for box in boxes:
            print("{:<10} {:<15} {:<15} {:<20} {:<10} ${:<10.2f}".format(
                box.id, box.name, box.material, box.dimensions, 
                box.weight, box.price))

    @staticmethod
    # Display system messages
    def display_message(message):
        print(f"\n📌 {message}")
