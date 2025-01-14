class View:
    def display_menu(self):
        # Display the main menu and return the user's choice.
        print("\nWelcome to the Bird Study Service by David Caleb")
        print("1. View all birds")
        print("2. Add new bird")
        print("3. Remove bird")
        print("4. Search for a bird")
        print("5. Update a bird's name")
        print("6. Count total number of birds")
        print("7. Exit")
        
        return input("Please enter your choice: ")

    def show_all_birds(self, birds):
        # Display all birds in the study.
        if not birds:
            print("No birds found.")
        else:
            print("\nList of Birds:")
            for bird in birds:
                print(f"- {bird}")

    def get_new_bird_info(self):
        # Prompt user for new bird information.
        return input("Enter the name of the new bird: ")

    def get_bird_to_remove(self):
        # Prompt user for the name of the bird to remove.
        return input("Enter the name of the bird to remove: ")

    def get_bird_to_search(self):
        # Prompt user for the name of the bird to search.
        return input("Enter the name of the bird to search: ")

    def get_old_bird_info(self):
        # Prompt user for the old name of the bird to update.
        return input("Enter the current name of the bird you want to update: ")

    def show_message(self, message):
        # Display a message to the user.
        print(message)
