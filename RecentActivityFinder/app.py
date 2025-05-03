# Import necessary libraries
import os
import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class RecentFileFinder:
    def __init__(self, root):
        self.root = root
        self.root.title("Recent File Finder by David Caleb")
        self.root.geometry("600x400")
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6)
        self.style.configure("TLabel", padding=6)
        
        # Create UI elements
        self.create_widgets()
        
    # Create and arrange all GUI components
    def create_widgets(self):
        # Frame for directory selection
        dir_frame = ttk.Frame(self.root, padding="10")
        dir_frame.pack(fill=tk.X)
        
        ttk.Label(dir_frame, text="Directory:").pack(side=tk.LEFT)
        
        self.dir_entry = ttk.Entry(dir_frame, width=50)
        self.dir_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        
        browse_btn = ttk.Button(
            dir_frame, 
            text="Browse...", 
            command=self.select_directory
        )
        browse_btn.pack(side=tk.LEFT)
        
        # Frame for controls
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.pack(fill=tk.X)
        
        ttk.Label(control_frame, text="Number of files to show:").pack(side=tk.LEFT)
        
        self.num_files = tk.IntVar(value=10)
        num_spin = ttk.Spinbox(
            control_frame,
            from_=1,
            to=100,
            textvariable=self.num_files,
            width=5
        )
        num_spin.pack(side=tk.LEFT, padx=5)
        
        search_btn = ttk.Button(
            control_frame,
            text="Find Recent Files",
            command=self.find_recent_files
        )
        search_btn.pack(side=tk.LEFT, padx=10)
        
        # Results display
        results_frame = ttk.Frame(self.root)
        results_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=(0, 10))
        
        # Treeview with scrollbar
        self.tree = ttk.Treeview(
            results_frame,
            columns=("File", "Modified", "Size"),
            show="headings",
            selectmode="browse"
        )
        
        # Configure columns
        self.tree.heading("File", text="File Path")
        self.tree.heading("Modified", text="Last Modified")
        self.tree.heading("Size", text="Size (KB)")
        
        self.tree.column("File", width=300, anchor=tk.W)
        self.tree.column("Modified", width=150, anchor=tk.W)
        self.tree.column("Size", width=100, anchor=tk.E)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(
            results_frame,
            orient=tk.VERTICAL,
            command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Layout tree and scrollbar
        self.tree.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    # Open directory dialog and update entry field
    def select_directory(self):
        directory = filedialog.askdirectory(title="Select Directory to Scan")
        if directory:
            self.dir_entry.delete(0, tk.END)
            self.dir_entry.insert(0, directory)
    
    # Find and display recent files in selected directory
    def find_recent_files(self):
        directory = self.dir_entry.get()
        num_files = self.num_files.get()
        
        if not directory or not os.path.isdir(directory):
            messagebox.showerror(
                "Error",
                "Please select a valid directory first!"
            )
            return
        
        try:
            # Clear previous results
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Get files and sort by modification time
            files = []
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isfile(item_path):
                    mod_time = os.path.getmtime(item_path)
                    file_size = os.path.getsize(item_path) / 1024  # KB
                    files.append((
                        item_path,
                        datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M:%S"),
                        f"{file_size:,.1f}"
                    ))
            
            # Sort by modification time (newest first)
            files.sort(key=lambda x: x[1], reverse=True)
            
            # Display results
            for file_info in files[:num_files]:
                self.tree.insert("", tk.END, values=file_info)
                
            if not files:
                messagebox.showinfo(
                    "No Files Found",
                    "The selected directory contains no files."
                )
                
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An error occurred while scanning files:\n{str(e)}"
            )

def main():
    root = tk.Tk()
    app = RecentFileFinder(root)
    root.mainloop()

if __name__ == "__main__":
    main()