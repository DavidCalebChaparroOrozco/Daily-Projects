from model.model import LotionModel, Lotion 
from view.view import LotionView

class LotionController:
    def __init__(self):
        self.model = LotionModel()
    
    def run(self):
        while True:
            LotionView.display_menu()
            choice = input("Choose an option: ")

            if choice == '1':
                lotions = self.model.get_all_lotions()
                LotionView.display_lotions(lotions)

            elif choice == '2':
                new_lotion_details = LotionView.get_lotion_details()
                new_lotion = Lotion(*new_lotion_details)  
                self.model.add_lotion(new_lotion)
                LotionView.display_success_message("Lotion added successfully.")

            elif choice == '3':
                lotion_id = LotionView.get_lotion_id()
                if self.model.remove_lotion(lotion_id):
                    LotionView.display_success_message("Lotion removed successfully.")
                else:
                    LotionView.display_error_message("Lotion ID not found.")

            elif choice == '4':
                lotion_id, new_stock = LotionView.get_lotion_stock_update()
                lotion = self.model.find_lotion_by_id(lotion_id)
                if lotion:
                    lotion.stock = new_stock
                    LotionView.display_success_message("Lotion stock updated successfully.")
                else:
                    LotionView.display_error_message("Lotion ID not found.")

            elif choice == '5':
                print("Exiting the application.")
                break
            
            else:
                LotionView.display_error_message("Invalid option. Please try again.")