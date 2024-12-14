from controller.controller import CharacterPresenter
from view.view import CharacterView

def main():
    presenter = CharacterPresenter()
    
    while True:
        CharacterView.display_menu()
        
        choice = input("Select an option: ")
        
        if choice == '1':
            characters = presenter.get_characters()
            CharacterView.show_characters(characters)
        
        elif choice == '2':
            name, mythology, description = CharacterView.get_character_input()
            presenter.add_character(name, mythology, description)
            print(f"Character '{name}' added successfully.")
        
        elif choice == '3':
            name = CharacterView.get_character_name()
            presenter.remove_character(name)
            print(f"Character '{name}' removed successfully.")
        
        elif choice == '4':
            name = CharacterView.get_specific_character_name()
            character = presenter.get_character_by_name(name)
            CharacterView.show_specific_character(character)

        elif choice == '5':
            old_name, new_name, new_mythology, new_description = CharacterView.get_update_input()
            presenter.update_character(old_name, new_name, new_mythology, new_description)
            print(f"Character '{old_name}' updated successfully.")
        
        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
