class RoleView:
    @staticmethod
    def display_menu():
        print("\nWelcome to the Team Management System by David Caleb")
        print("1. View all roles")
        print("2. Add new role")
        print("3. Remove role")
        print("4. View specific role")
        print("5. Update existing role")
        print("6. Exit")

    @staticmethod
    def show_roles(roles):
        if not roles:
            print("No roles available.")
            return
        print("\nCurrent Roles:")
        for role in roles:
            print(f"- {role.title}: {role.description}")

    @staticmethod
    def get_role_input():
        title = input("Enter role title: ")
        description = input("Enter role description: ")
        return title, description

    @staticmethod
    def get_role_title():
        return input("Enter the title of the role to remove: ")

    @staticmethod
    def get_specific_role_title():
        return input("Enter the title of the role to view: ")

    @staticmethod
    def get_update_input():
        old_title = input("Enter the current title of the role to update: ")
        new_title = input("Enter the new title: ")
        new_description = input("Enter the new description: ")
        return old_title, new_title, new_description

    @staticmethod
    def show_specific_role(role):
        if not role:
            print("Role not found.")
            return
        print(f"\nRole Details:\n- Title: {role.title}\n- Description: {role.description}")