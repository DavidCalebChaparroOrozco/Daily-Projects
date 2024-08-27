# Importing necessary libraries
import os
from file_manager import Directory

# Function to display the menu
def display_menu():
    print("\nFile Manager Pro by David Caleb")
    print("1. Create a new file")
    print("2. Create a new folder")
    print("3. Find a file or folder path")
    print("4. List all contents of a folder")
    print("5. Calculate total size of all files")
    print("6. Delete all files with a specific extension")
    print("7. Exit")
    print("=".center(50,"="))
    return input("Select an option: ")

# Main code
if __name__ == "__main__":
    base_path = input("Enter the base directory path: ")
    directory = Directory(base_path)

    while True:
        option = display_menu()

        if option == "1":
            # Create a new file
            file_name = input("Enter the file name: ")
            extension = input("Enter the file extension: ")
            size = int(input("Enter the file size in bytes: "))
            owner = input("Enter the owner's name: ")
            directory.create_file(file_name, extension, size, owner)
            print("File created successfully.")

        elif option == "2":
            # Create a new folder
            folder_name = input("Enter the folder name: ")
            directory.create_folder(folder_name)
            print("Folder created successfully.")

        elif option == "3":
            # Find a file or folder path
            search_name = input("Enter the file or folder name to find: ")
            path = directory.find_path(search_name)
            if path:
                print(f"Path found: {path}")
            else:
                print("File or folder not found.")

        elif option == "4":
            # List all contents of a folder
            contents = directory.list_contents()
            print("Contents of the directory:")
            for item in contents:
                print(f" - {item}")

        elif option == "5":
            # Calculate total size of all files
            total_size = directory.calculate_total_size()
            print(f"Total size of all files: {total_size} bytes")

        elif option == "6":
            # Delete all files with a specific extension
            extension = input("Enter the file extension to delete (e.g., txt): ")
            directory.delete_files_by_extension(extension)
            print(f"All files with .{extension} extension deleted.")

        elif option == "7":
            # Exit
            print("Exiting File Manager Pro.")
            break

        else:
            print("Invalid option. Please try again.")
