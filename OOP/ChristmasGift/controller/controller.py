from model.model import Gift, GiftModel
from view.view import GiftView, GiftSortOption

# Controller class to manage user interactions and data flow.
class GiftController:
    
    def __init__(self):
        self.model = GiftModel()
        self.view = GiftView()

    def run(self):        
        while True:
            self.view.display_menu()
            choice = input("Choose an option (1-7): ")

            if choice == '1':
                gifts = self.model.get_all_gifts()
                self.view.display_gifts(gifts)
            elif choice == '2':
                name, description, category = self.view.get_new_gift_info()
                new_gift = Gift(name, description, category)
                self.model.add_gift(new_gift)
                print(f"Gift '{name}' added successfully!")
            elif choice == '3':
                name = self.view.get_gift_name()
                self.model.remove_gift(name)
                print(f"Gift '{name}' removed successfully!")
            elif choice == '4':
                old_name = self.view.get_gift_name()
                new_name, new_description, new_category = self.view.get_updated_gift_info()
                updated_gift = Gift(new_name, new_description, new_category)
                self.model.update_gift(old_name, updated_gift)
                print(f"Gift '{old_name}' updated successfully!")
            elif choice == '5':
                keyword = self.view.get_search_keyword()
                matching_gifts = self.model.search_gift(keyword)
                if matching_gifts:
                    print("\nMatching Gifts:")
                    self.view.display_gifts(matching_gifts)
                else:
                    print("No matching gifts found.")
            elif choice == '6':
                sort_option = int(self.view.get_sort_option())
                if sort_option == 1:
                    sorted_gifts = self.model.sort_gifts(GiftSortOption.NAME)
                    print("\nGifts sorted by Name:")
                    self.view.display_gifts(sorted_gifts)
                elif sort_option == 2:
                    sorted_gifts = self.model.sort_gifts(GiftSortOption.CATEGORY)
                    print("\nGifts sorted by Category:")
                    self.view.display_gifts(sorted_gifts)
                elif sort_option == 3:
                    sorted_gifts = self.model.sort_gifts(GiftSortOption.DATE_ADDED)
                    print("\nGifts sorted by Date Added:")
                    self.view.display_gifts(sorted_gifts)
                else:
                    print("Invalid sorting option.")
            elif choice == '7':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
