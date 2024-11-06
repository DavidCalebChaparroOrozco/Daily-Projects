from model.model import HouseModel
from view.view import HouseView

class HouseController:
    def __init__(self):
        self.model = HouseModel()
        self.view = HouseView()

    def run(self):
        while True:
            self.view.display_menu()
            choice = input("Select an option (1-4): ")

            if choice == '1':
                houses = self.model.get_all_houses()
                self.view.display_houses(houses)
            elif choice == '2':
                address, rent, bedrooms, bathrooms = self.view.get_house_details()
                self.model.add_house(address, rent, bedrooms, bathrooms)
                self.view.display_success_message("House added successfully.")
            elif choice == '3':
                house_id = self.view.get_house_id()
                if self.model.remove_house(house_id):
                    self.view.display_success_message("House removed successfully.")
                else:
                    self.view.display_error_message("House ID not found.")
            elif choice == '4':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please select a valid option.")