# Class to handle the display of gifts and menus.
class GiftView:
    
    @staticmethod
    # Display the main menu options.
    def display_menu():
        print("\nWelcome to the Christmas Gift Manager by David Caleb")
        print("1. View all gifts")
        print("2. Add new gift")
        print("3. Remove a gift")
        print("4. Update a gift")
        print("5. Search for a gift")
        print("6. Sort gifts")
        print("7. Exit")

    @staticmethod
    # Display all gifts in a formatted manner.
    def display_gifts(gifts):
        if not gifts:
            print("No gifts available.")
            return
        print("\nList of Gifts:")
        for gift in gifts:
            print(f" - {gift}")

    @staticmethod
    # Prompt user for new gift information.
    def get_new_gift_info():
        name = input("Enter the name of the gift: ")
        description = input("Enter a description for the gift: ")
        category = input("Enter the category of the gift: ")
        return name, description, category

    @staticmethod
    # Prompt user for the name of the gift to remove or update.
    def get_gift_name():
        return input("Enter the name of the gift: ")

    @staticmethod
    # Prompt user for updated gift information.
    def get_updated_gift_info():
        name = input("Enter the new name of the gift: ")
        description = input("Enter a new description for the gift: ")
        category = input("Enter the new category of the gift: ")
        return name, description, category
    
    @staticmethod
    # Prompt user for a keyword to search gifts.
    def get_search_keyword():
        return input("Enter keyword to search for gifts: ")

    @staticmethod
    # Prompt user for sorting option.
    def get_sort_option():
        print("\nSort by:")
        print("1. Name")
        print("2. Category")
        print("3. Date Added")
        
        # Get user input and return it
        return input("Choose sorting option (1-3):")
        
class GiftSortOption:
    NAME = "name"
    CATEGORY = "category"
    DATE_ADDED = "date_added"