from controller.controller import RoleController
from view.view import RoleView

def main():
    controller = RoleController()
    
    while True:
        RoleView.display_menu()
        
        choice = input("Select an option: ")
        
        if choice == '1':
            roles = controller.get_roles()
            RoleView.show_roles(roles)
        
        elif choice == '2':
            title, description = RoleView.get_role_input()
            controller.add_role(title, description)
            print(f"Role '{title}' added successfully.")
        
        elif choice == '3':
            title = RoleView.get_role_title()
            controller.remove_role(title)
            print(f"Role '{title}' removed successfully.")
        
        elif choice == '4':
            title = RoleView.get_specific_role_title()
            role = controller.get_role_by_title(title)
            RoleView.show_specific_role(role)

        elif choice == '5':
            old_title, new_title, new_description = RoleView.get_update_input()
            controller.update_role(old_title, new_title, new_description)
            print(f"Role '{old_title}' updated to '{new_title}' successfully.")
        
        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()