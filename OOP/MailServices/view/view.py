class View:
    def display_menu(self):
        print("\nWelcome to the Package Service by David Caleb")
        print("1. View all packages")
        print("2. Add new package")
        print("3. Remove package")
        print("4. Modify package")
        print("5. Search for a package")
        print("6. Filter packages by weight")
        print("7. Sort packages by weight")
        print("8. View statistics")
        print("9. Save packages to a file")
        print("10. Load packages from a file")
        print("11. Exit")
        
        return input("Please choose an option: ")

    def show_packages(self, packages):
        if not packages:
            print("No packages available.")
            return
        
        print("\nAll Packages:")
        for pkg in packages:
            print(f"ID: {pkg['id']}, Description: {pkg['description']}, Weight: {pkg['weight']} kg")

    # Get information about a new or modified package from the user.
    def get_package_info(self):
        package_id = input("Enter package ID: ")
        description = input("Enter package description: ")
        weight = float(input("Enter package weight (kg): "))
        
        return {"id": package_id, "description": description, "weight": weight}

    # Get the ID of the package to remove or modify from the user.
    def get_package_id(self, action):
        return input(f"Enter package ID to {action}: ")

    # Get search term from the user.
    def get_search_term(self):
        return input("Enter ID or description to search: ")

    # Get weight limit for filtering from the user.
    def get_weight_filter(self):
        return float(input("Enter maximum weight limit (kg): "))

    # Get filename for saving or loading from the user.
    def get_filename(self, action):
        return input(f"Enter filename to {action} (with .json or .csv extension): ")

    # Get file type (JSON or CSV) from the user.
    def get_filetype(self):
        return input("Enter file type (json/csv): ").lower()

    def show_statistics(self, stats):
        print("\nStatistics:")
        print(f"Total Packages: {stats['total_packages']}")
