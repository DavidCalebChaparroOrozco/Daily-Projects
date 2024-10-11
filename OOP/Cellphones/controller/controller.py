from model.cellphone import Cellphone, Inventory
from view.view import View

class Controller:
    def __init__(self):
        # Initializes the controller with an empty inventory
        self.inventory = Inventory()
        self.view = View()

    def run(self):
        # Main loop for the program
        while True:
            # Display the menu and get user choice
            self.view.display_menu()
            choice = self.view.get_user_choice()

            if choice == '1':
                # Add new cellphone to inventory
                self.add_cellphone()
            elif choice == '2':
                # Update stock of an existing cellphone
                self.update_stock()
            elif choice == '3':
                # View all cellphones in the inventory
                self.view_cellphones()
            elif choice == '4':
                # Exit the program
                self.view.show_message("Exiting... Goodbye!")
                break
            else:
                # Invalid input
                self.view.show_message("Invalid choice. Please select a valid option.")

    def add_cellphone(self):
        # Gets cellphone details from the user and adds it to inventory
        model_name, brand, stock = self.view.get_cellphone_details()
        cellphone = Cellphone(model_name, brand, stock)
        self.inventory.add_cellphone(cellphone)
        self.view.show_message("Cellphone added successfully!")

    def update_stock(self):
        # Gets model name and new stock, updates the inventory
        model_name = self.view.get_model_name()
        cellphone = self.inventory.find_cellphone(model_name)
        if cellphone:
            new_stock = self.view.get_new_stock()
            cellphone.update_stock(new_stock)
            self.view.show_message(f"Stock for {model_name} updated to {new_stock}.")
        else:
            self.view.show_message("Cellphone not found in inventory.")

    def view_cellphones(self):
        # Retrieves and displays all cellphones from the inventory
        cellphones = self.inventory.get_inventory()
        self.view.display_cellphones(cellphones)
