# Importing necessary libraries
import tkinter as tk
from tkinter import ttk, messagebox
from database import create_table, insert_item, get_items, delete_item
import re

class HouseholdBasketApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.title("Household Basket by David Caleb")
        self.geometry("600x500")
        self.configure(bg='#333333')

        # Initialize the database table
        create_table()

        # Create and place widgets
        self.create_widgets()

    # Create and place the GUI widgets
    def create_widgets(self):
        # Category label and combobox
        self.category_label = tk.Label(self, text="Category:", bg='#333333', fg='white')
        self.category_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.category_var = tk.StringVar()
        self.category_combobox = ttk.Combobox(self, textvariable=self.category_var, state='readonly')
        self.category_combobox['values'] = ('Fruit', 'Vegetable', 'Meat', 'Dairy', 'Other')
        self.category_combobox.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        self.category_combobox.set('Fruit')  # Set default value to 'Fruit'

        # Name label and entry
        self.name_label = tk.Label(self, text="Name:", bg='#333333', fg='white')
        self.name_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.name_entry = tk.Entry(self, bg='#f7f7f7', fg='#333333')
        self.name_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        self.name_entry.bind('<KeyRelease>', self.validate_name)  # Bind key release event to validate name

        # Quantity label and entry
        self.quantity_label = tk.Label(self, text="Quantity:", bg='#333333', fg='white')
        self.quantity_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.quantity_entry = tk.Entry(self, bg='#f7f7f7', fg='#333333')
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.quantity_entry.bind('<KeyRelease>', self.validate_quantity)  # Bind key release event to validate quantity

        # Add item button
        self.add_button = tk.Button(self, text="Add Item", command=self.add_item, bg='#4CAF50', fg='white')
        self.add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        # Treeview to display items
        self.items_tree = ttk.Treeview(self, columns=("ID", "Category", "Name", "Quantity"), show='headings')
        self.items_tree.heading("ID", text="ID")
        self.items_tree.heading("Category", text="Category")
        self.items_tree.heading("Name", text="Name")
        self.items_tree.heading("Quantity", text="Quantity")
        self.items_tree.column("ID", width=30)
        self.items_tree.column("Category", width=100)
        self.items_tree.column("Name", width=150)
        self.items_tree.column("Quantity", width=70)
        self.items_tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Delete item button
        self.delete_button = tk.Button(self, text="Delete Item", command=self.delete_item, bg='#f44336', fg='white')
        self.delete_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        # Configure grid weights for proper resizing
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Load the items from the database into the treeview
        self.load_items()

    # Add a new item to the database and refresh the treeview
    def add_item(self):
        category = self.category_var.get()
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()

        if category and name and quantity.isdigit() and int(quantity) > 0:
            insert_item(category, name, int(quantity))
            self.load_items()
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields correctly")

    # Load items from the database into the treeview
    def load_items(self):
        for item in self.items_tree.get_children():
            self.items_tree.delete(item)

        items = get_items()
        for item in items:
            self.items_tree.insert('', 'end', values=item)

    # Clear the input fields
    def clear_entries(self):
        self.category_combobox.set('Fruit')
        self.name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    # Delete the selected item from the database and refresh the treeview
    def delete_item(self):
        selected_item = self.items_tree.selection()
        if selected_item:
            item_id = self.items_tree.item(selected_item[0])['values'][0]
            delete_item(item_id)
            self.load_items()
        else:
            messagebox.showwarning("Selection Error", "Please select an item to delete")

    # Validate the name field to allow only characters
    def validate_name(self, event):
        name = self.name_entry.get()
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, re.sub(r'[^a-zA-Z]', '', name))

    # Validate the quantity field to be greater than 0
    def validate_quantity(self, event):
        quantity = self.quantity_entry.get()
        self.quantity_entry.delete(0, tk.END)
        self.quantity_entry.insert(0, re.sub(r'\D', '', quantity))

# Main entry point of the application
if __name__ == "__main__":
    app = HouseholdBasketApp()
    app.mainloop()