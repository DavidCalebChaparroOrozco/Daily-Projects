# Import necessary libraries
import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog

# Open a dialog to select the target folder for organization.
def select_target_folder():
    root = tk.Tk()
    # Hide the main window
    root.withdraw()  
    
    # Ask user to select folder
    folder_path = filedialog.askdirectory(
        title="Select Folder to Organize"
    )
    
    if not folder_path:  
        # User cancelled
        print("\nNo folder selected. Exiting...")
        return None
    
    return folder_path

# Create necessary subfolders if they don't exist.
# Returns dictionary of folder categories and their extensions.
def create_folders(target_path):
    folders = {
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv', '.odt', '.rtf'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm'],
        'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        'Installers': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm'],
        'Code': ['.py', '.js', '.html', '.css', '.json', '.cpp', '.java', '.php'],
        # For files with unclassified extensions
        'Others': []  
    }
    
    print("\nCreating folders...")
    for folder in folders.keys():
        folder_path = os.path.join(target_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created: {folder}")
        else:
            print(f"Exists: {folder}")
    
    return folders

# Move files to their corresponding folders based on extensions.
# Returns count of moved files and list of unclassified extensions found.
def organize_files(target_path, folders):
    moved_files = 0
    unclassified_exts = set()
    
    for filename in os.listdir(target_path):
        file_path = os.path.join(target_path, filename)
        
        # Skip if it's a directory or this script file
        if os.path.isdir(file_path) or filename == os.path.basename(__file__):
            continue
        
        # Get file extension
        _, file_ext = os.path.splitext(filename)
        # Make case-insensitive
        file_ext = file_ext.lower()  
        
        # Find the appropriate folder
        destination_folder = 'Others'
        for folder, extensions in folders.items():
            if file_ext in extensions:
                destination_folder = folder
                break
        else:
            # Only track non-empty extensions
            if file_ext:  
                unclassified_exts.add(file_ext)
        
        # Move the file
        destination_path = os.path.join(target_path, destination_folder, filename)
        
        try:
            shutil.move(file_path, destination_path)
            print(f"Moved: {filename.ljust(30)} -> {destination_folder}")
            moved_files += 1
        except Exception as e:
            print(f"Error moving {filename}: {str(e)}")
    
    return moved_files, unclassified_exts

def main():
    print("\n SmartFolder by David Caleb")
    print("Please select the folder you want to organize...")
    
    # Get target folder from user
    target_path = select_target_folder()
    if not target_path:
        return
    
    print(f"\nSelected folder: {target_path}")
    
    # Create necessary folders
    folders = create_folders(target_path)
    
    # Organize files
    print("\nOrganizing files...")
    start_time = time.time()
    moved_files, unclassified_exts = organize_files(target_path, folders)
    elapsed_time = time.time() - start_time
    
    # Display summary
    print("\n Organization Summary ")
    print(f"Target folder: {target_path}")
    print(f"Total files moved: {moved_files}")
    
    if unclassified_exts:
        print("\nUnclassified extensions found:")
        for ext in sorted(unclassified_exts):
            print(f"- {ext}")
        print("\nYou can add these extensions to the appropriate category in the script.")
    
    print(f"\nTime elapsed: {elapsed_time:.2f} seconds")
    print("Organization complete!")

if __name__ == "__main__":
    main()