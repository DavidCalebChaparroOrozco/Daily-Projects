# Importing necessary libraries
import os

class Directory:
    # Constructor to initialize the directory object with a base path
    def __init__(self, base_path):
        self.base_path = base_path

    # Method to create a new file within the directory
    def create_file(self, name, extension, size, owner):
        # Construct the full path of the file
        full_path = os.path.join(self.base_path, f"{name}.{extension}")
        
        # Ensure the directory exists before creating the file
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Create the file and write placeholder data to simulate the specified size
        with open(full_path, 'w') as file:
            file.write(' ' * size)  
        
        # Print a confirmation message
        print(f"File '{full_path}' created with size {size} bytes.")

    # Method to create a new folder within the directory
    def create_folder(self, folder_name):
        # Construct the full path of the folder
        full_path = os.path.join(self.base_path, folder_name)
        
        # Create the folder, ensuring it exists without raising an error if it already does
        os.makedirs(full_path, exist_ok=True)
        
        # Print a confirmation message
        print(f"Folder '{full_path}' created.")

    # Method to find the path of a given file or folder within the directory
    def find_path(self, name):
        # Walk through the directory tree to find the specified name
        for root, dirs, files in os.walk(self.base_path):
            if name in dirs or name in files:
                return os.path.join(root, name)
        return None

    # Method to list the contents of the base directory
    def list_contents(self):
        # Return a list of files and folders in the base directory
        return os.listdir(self.base_path)

    # Method to calculate the total size of all files within the directory
    def calculate_total_size(self):
        total_size = 0
        # Walk through the directory tree and sum the sizes of all files
        for dirpath, dirnames, filenames in os.walk(self.base_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    # Method to delete files with a specified extension within the directory
    def delete_files_by_extension(self, extension):
        # Walk through the directory tree and delete files with the specified extension
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                if file.endswith(f".{extension}"):
                    os.remove(os.path.join(root, file))
                    print(f"Deleted file: {os.path.join(root, file)}")