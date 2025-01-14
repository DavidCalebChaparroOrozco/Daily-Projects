from model.model import BirdStudy
from view.view import View

class Controller:
    def __init__(self):
        self.bird_study = BirdStudy()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.display_menu()
            if choice == '1':
                self.view.show_all_birds(self.bird_study.get_all_birds())
            elif choice == '2':
                bird_name = self.view.get_new_bird_info()
                self.bird_study.add_bird(bird_name)
                self.view.show_message(f"Added bird: {bird_name}")
            elif choice == '3':
                bird_name = self.view.get_bird_to_remove()
                if self.bird_study.remove_bird(bird_name):
                    self.view.show_message(f"Removed bird: {bird_name}")
                else:
                    self.view.show_message("Bird not found.")
            elif choice == '4':
                search_name = self.view.get_bird_to_search()
                result = self.bird_study.search_bird(search_name)
                if result:
                    self.view.show_message(f"Bird found: {result}")
                else:
                    self.view.show_message("Bird not found.")
            elif choice == '5':
                old_name = self.view.get_old_bird_info()
                new_name = self.view.get_new_bird_info()
                if self.bird_study.update_bird(old_name, new_name):
                    self.view.show_message(f"Updated bird: {old_name} to {new_name}")
                else:
                    self.view.show_message("Bird not found for update.")
            elif choice == '6':
                count = self.bird_study.count_birds()
                self.view.show_message(f"Total number of birds: {count}")
            elif choice == '7':
                self.view.show_message("Exiting the program.")
                break
            else:
                self.view.show_message("Invalid choice. Please try again.")