# Importing necessary libraries
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import pandas as pd

class DashboardApp:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Custom Dashboard Generator by David Caleb")

        # Set background color for the window
        self.parent.configure(bg="#f0f0f0")

        # Create a Frame to hold the dashboard widgets
        self.dashboard_frame = ttk.Frame(parent, padding="10")
        self.dashboard_frame.grid(sticky="nsew")

        # Initialize variables for data and selections
        self.data = None
        
        # Create and place widgets on the dashboard using the Grid geometry manager
        self.create_widgets()

    def create_widgets(self):
        # Label for file upload
        label_upload = tk.Label(self.dashboard_frame, text="Upload Dataset (CSV/XLS/XLSX):", bg="#f0f0f0")
        label_upload.grid(row=0, column=0, padx=10, pady=10)

        # Button to upload file with improved UI
        btn_upload = tk.Button(self.dashboard_frame, text="Browse", command=self.load_data,
                                bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5)
        btn_upload.grid(row=0, column=1, padx=10, pady=10)

        # Dropdown for selecting columns to visualize
        self.column_selection = ttk.Combobox(self.dashboard_frame)
        self.column_selection.grid(row=1, column=0, padx=10, pady=10)
        
        # Button to plot selected graph type with improved UI
        btn_plot = tk.Button(self.dashboard_frame, text="Plot Graph", command=self.plot_graph,
                            bg="#2196F3", fg="white", font=("Arial", 12), padx=10, pady=5)
        btn_plot.grid(row=1, column=1, padx=10, pady=10)

        # Label for graph type selection
        label_graph_type = tk.Label(self.dashboard_frame, text="Select Graph Type:", bg="#f0f0f0")
        label_graph_type.grid(row=2, column=0, padx=10, pady=10)

        # Dropdown for graph type selection
        self.graph_type_selection = ttk.Combobox(self.dashboard_frame, values=["Bar", "Line", "Pie"])
        self.graph_type_selection.grid(row=2, column=1, padx=10, pady=10)

    def load_data(self):
        # Open file dialog to select CSV or Excel files
        file_path = filedialog.askopenfilename(filetypes=[
            ("CSV files", "*.csv"),
            ("Excel files", "*.xls;*.xlsx"),
            ("All files", "*.*")
        ])
        
        if file_path:
            try:
                # Load the dataset into a pandas DataFrame based on the file extension
                if file_path.endswith('.csv'):
                    self.data = pd.read_csv(file_path)
                elif file_path.endswith('.xls'):
                    # Use 'xlrd' for .xls files
                    self.data = pd.read_excel(file_path, engine='xlrd')  
                elif file_path.endswith('.xlsx'):
                    # Use 'openpyxl' for .xlsx files
                    self.data = pd.read_excel(file_path, engine='openpyxl')  
                
                # Update column selection dropdown with available columns in the dataset
                self.column_selection['values'] = list(self.data.columns)

            except ValueError as e:
                messagebox.showerror("File Error", f"Error reading the file: {e}")
            except Exception as e:
                messagebox.showerror("Unexpected Error", f"An unexpected error occurred: {e}")

    def plot_graph(self):
        # Check if data is loaded and selections are valid
        if self.data is None or self.data.empty or not self.column_selection.get() or not self.graph_type_selection.get():
            return  # Exit if data is not loaded or selections are invalid

        selected_column = self.column_selection.get()
        graph_type = self.graph_type_selection.get()

        # Ensure the selected column exists in the DataFrame
        if selected_column not in self.data.columns:
            # Exit if the selected column is invalid
            return  

        plt.figure(figsize=(8, 6))  # Set figure size

        # Plot based on selected graph type
        if graph_type == "Bar":
            ax = self.data[selected_column].value_counts().plot(kind='bar')
            plt.title(f'Bar Graph of {selected_column}')
            plt.xticks(rotation=45)
            
        elif graph_type == "Line":
            plt.plot(self.data[selected_column])
            plt.title(f'Line Graph of {selected_column}')
            plt.xticks(rotation=45)  
            
        elif graph_type == "Pie":
            self.data[selected_column].value_counts().plot(kind='pie', autopct='%1.1f%%')
            plt.title(f'Pie Chart of {selected_column}')
        
        # Adjust layout to make room for rotated labels
        plt.tight_layout()  
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
