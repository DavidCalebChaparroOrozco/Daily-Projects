# Importing necessary libraries
from abc import ABC, abstractmethod
import os

# Base Class for File and Folder
class FileSystemItem(ABC):
    def __init__(self, name, path):
        # Encapsulation: Making attributes private
        self._name = name
        self._path = path

    @abstractmethod
    def get_description(self):
        """
        Abstract method to get the description of the file or folder.
        Subclasses must implement this method.
        """
        pass

    # Getter method to retrieve the name of the file or folder
    def get_name(self):
        return self._name

    # Getter method to retrieve the path of the file or folder
    def get_path(self):
        return self._path


# Inheritance for File
class File(FileSystemItem):
    def __init__(self, name, path, size):
        super().__init__(name, path)
        self._size = size

    # Implement the abstract method to get the description of the file
    def get_description(self):
        return f"File: {self.get_name()} (Path: {self.get_path()}, Size: {self._size} bytes)"


# Inheritance for Folder
class Folder(FileSystemItem):
    def __init__(self, name, path):
        super().__init__(name, path)
        self._files = []

    # Implement the abstract method to get the description of the folder
    def get_description(self):
        return f"Folder: {self.get_name()} (Path: {self.get_path()})"

    # Method to add a file to the folder
    def add_file(self, file):
        self._files.append(file)

    # Method to get the list of files in the folder
    def get_files(self):
        return self._files


# Class for File Operation
class FileOperation:
    def __init__(self, file, operation_type, operation_date):
        self._file = file
        self._operation_type = operation_type
        self._operation_date = operation_date

    # Method to get the operation details
    def get_details(self):
        return (f"Operation: {self._operation_type} on {self._file.get_name()} "
                f"at {self._operation_date}")


# Function to display the menu
def display_menu():
    print("\nFile System Management")
    print("1. Register new file")
    print("2. Register new folder")
    print("3. Perform file operation")
    print("4. Display file details")
    print("5. Display folder details")
    print("6. Exit")
    print("=".center(50, "="))
    return input("Select an option: ")


# Main code
if __name__ == "__main__":
    # Dictionary to hold files
    files = {}

    # Dictionary to hold folders
    folders = {}

    while True:
        option = display_menu()

        if option == "1":
            # Register new file
            file_name = input("Enter file name: ")
            file_path = input("Enter file path: ")
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                if file_name not in files:
                    files[file_name] = File(file_name, file_path, file_size)
                    print("File registered successfully.")
                else:
                    print("File name already exists.")
            else:
                print("File path does not exist.")

        elif option == "2":
            # Register new folder
            folder_name = input("Enter folder name: ")
            folder_path = input("Enter folder path: ")
            if os.path.exists(folder_path) and os.path.isdir(folder_path):
                if folder_name not in folders:
                    folders[folder_name] = Folder(folder_name, folder_path)
                    print("Folder registered successfully.")
                else:
                    print("Folder name already exists.")
            else:
                print("Folder path does not exist or is not a directory.")

        elif option == "3":
            # Perform file operation
            file_name = input("Enter file name: ")
            if file_name in files:
                operation_type = input("Enter operation type (read/write/execute): ")
                operation_date = input("Enter operation date (YYYY-MM-DD): ")
                file = files[file_name]
                file_operation = FileOperation(file, operation_type, operation_date)
                print(f"Operation performed: {file_operation.get_details()}")
            else:
                print("File not found.")

        elif option == "4":
            # Display file details
            file_name = input("Enter file name: ")
            if file_name in files:
                file = files[file_name]
                print(file.get_description())
            else:
                print("File not found.")

        elif option == "5":
            # Display folder details
            folder_name = input("Enter folder name: ")
            if folder_name in folders:
                folder = folders[folder_name]
                print(folder.get_description())
                for file in folder.get_files():
                    print(f" - {file.get_description()}")
            else:
                print("Folder not found.")

        elif option == "6":
            # Exit
            break

        else:
            print("Invalid option. Please try again.")
