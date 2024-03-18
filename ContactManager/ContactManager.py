## Import necessary libraries
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import csv
import os
import re
from tkcalendar import Calendar, DateEntry

## Define the ContactManager class
class ContactManager:
    ## Initialize the ContactManager class
    def __init__(self, root):
        ## Set up the main window
        self.root = root
        self.root.title("Contact Manager")
        ## Initialize empty lists to store contacts
        self.contacts = []
        self.original_contacts = []  # Original list of contacts
        
        ## Create entry fields for contact information
        fields = ["First Name", "Last Name", "Phone", "Genre", "Email", "Birthday"]
        self.entries = {}
        for field in fields:
            frame = tk.Frame(root)
            frame.pack(fill=tk.X)
            label = tk.Label(frame, text=field, width=10)
            label.pack(side=tk.LEFT)
            if field == "Genre":
                entry = ttk.Combobox(frame, values=["Female", "Male"])
                entry.set("Male")
            elif field == "Birthday":
                entry = DateEntry(frame, width=12, background='gray61', foreground="white", bd=2)
                entry.pack(side=tk.LEFT, padx=5)
                self.entries[field] = entry
                continue
            else:
                entry = tk.Entry(frame)
            if field == "First Name" or field == "Last Name":
                entry.config(validate="key", validatecommand=(root.register(self.validate_text), "%P"))
            elif field == "Phone":
                entry.config(validate="key", validatecommand=(root.register(self.validate_phone), "%P"))
            elif field == "Email":
                entry.config(validate="key", validatecommand=(root.register(self.validate_email), "%P"))
            entry.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
            self.entries[field] = entry
        
        ## Create buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        add_button = tk.Button(button_frame, text="Add", command=self.add_contact)
        add_button.pack(side=tk.LEFT, padx=5)
        view_button = tk.Button(button_frame, text="View Contacts", command=self.view_contacts)
        view_button.pack(side=tk.LEFT, padx=5)
        clear_button = tk.Button(button_frame, text="Clear", command=self.clear_fields)
        clear_button.pack(side=tk.LEFT, padx=5)
        exit_button = tk.Button(button_frame, text="Exit", command=root.quit)
        exit_button.pack(side=tk.LEFT, padx=5)
        self.contact_listbox = None
    
    ## Method to add a contact
    def add_contact(self):
        # Get values from entry fields
        contact_info = []
        for field, entry in self.entries.items():
            value = entry.get().strip()
            if not value:
                messagebox.showwarning("Missing Information", f"Please complete the {field} field.")
                return
            contact_info.append(value)
        self.contacts.append(contact_info)
        self.original_contacts.append(contact_info)  # Add to original list
        
        # Update contact listbox if initialized
        if self.contact_listbox:
            self.update_contact_listbox()
        self.clear_fields()
    
    ## Method to edit a contact
    def edit_contact(self):
        # Get selected contact
        selection = self.contact_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        if index < 0 or index >= len(self.contacts):
            return

        # Open edit window
        self.edit_window = tk.Toplevel(self.root)
        self.edit_window.title("Edit Contact")
        fields = ["First Name", "Last Name", "Phone", "Genre", "Email", "Birthday"]
        self.edit_entries = {}
        for field in fields:
            frame = tk.Frame(self.edit_window)
            frame.pack(fill=tk.X)
            label = tk.Label(frame, text=field, width=10)
            label.pack(side=tk.LEFT)
            if field == "Genre":
                entry = ttk.Combobox(frame, values=["Female", "Male"])
                entry.set("")
            elif field == "Birthday":
                entry = DateEntry(frame, width=12, background='gray61', foreground="white", bd=2)
                entry.pack(side=tk.LEFT, padx=5)
                self.edit_entries[field] = entry
                continue
            else:
                entry = tk.Entry(frame)
            entry.insert(0, self.contacts[index][fields.index(field)])
            if field == "First Name" or field == "Last Name":
                entry.config(validate="key", validatecommand=(self.root.register(self.validate_text), "%P"))
            elif field == "Phone":
                entry.config(validate="key", validatecommand=(self.root.register(self.validate_phone), "%P"))
            elif field == "Email":
                entry.config(validate="key", validatecommand=(self.root.register(self.validate_email), "%P"))
            entry.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
            self.edit_entries[field] = entry

        # Save button
        save_button = tk.Button(self.edit_window, text="Save", command=lambda: self.save_edited_contact(index))
        save_button.pack(pady=10)
    
    ## Method to save edited contact
    def save_edited_contact(self, index):
        contact_info = []
        for field, entry in self.edit_entries.items():
            contact_info.append(entry.get().strip())
        if contact_info[3] == "":
            messagebox.showwarning("Alert", "Genre field is empty. Please select a genre.")
            return
        self.contacts[index] = contact_info
        self.original_contacts[index] = contact_info  # Update in original list
        self.update_contact_listbox()
        self.edit_window.destroy()
    
    ## Method to view contacts
    def view_contacts(self):
        # Open view window
        view_window = tk.Toplevel(self.root)
        view_window.title("Contact List")
        self.page_number = 1
        self.contacts_per_page = 10
        
        # Search functionality
        search_frame = tk.Frame(view_window)
        search_frame.pack(pady=10)
        search_label = tk.Label(search_frame, text="Search:")
        search_label.pack(side=tk.LEFT)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        search_button = tk.Button(search_frame, text="Search", command=self.search_contacts)
        search_button.pack(side=tk.LEFT)
        self.contact_listbox = tk.Listbox(view_window)  # Assign self.contact_listbox
        self.contact_listbox.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        # Function to update contact list in ListBox
        self.update_contact_listbox()
        # Remaining buttons
        edit_button = tk.Button(view_window, text="Edit", command=self.edit_contact)
        edit_button.pack(side=tk.LEFT, padx=5)
        delete_button = tk.Button(view_window, text="Delete", command=self.delete_contact)
        delete_button.pack(side=tk.LEFT, padx=5)
        import_button = tk.Button(view_window, text="Import from CSV", command=self.import_from_csv)
        import_button.pack(side=tk.LEFT, padx=5)
        export_button = tk.Button(view_window, text="Export to CSV", command=self.export_to_csv)
        export_button.pack(side=tk.LEFT, padx=5)
        show_all_button = tk.Button(view_window, text="Show All", command=self.view_all_contacts)
        show_all_button.pack(side=tk.LEFT, padx=5)
        pagination_frame = tk.Frame(view_window)
        pagination_frame.pack(pady=10)
        previous_button = tk.Button(pagination_frame, text="Previous", command=self.previous_page)
        previous_button.pack(side=tk.LEFT, padx=5)
        next_button = tk.Button(pagination_frame, text="Next", command=self.next_page)
        next_button.pack(side=tk.LEFT, padx=5)
    
    ## Method to search contacts
    def search_contacts(self):
        search_term = self.search_entry.get().strip().lower()
        if not search_term:
            messagebox.showwarning("Warning", "Please enter a search term.")
            return
        
        results = []
        for contact in self.original_contacts:
            for field in contact:
                if search_term in field.lower():
                    results.append(contact)
                    break
        if results:
            self.contacts = results
            self.update_contact_listbox()
        else:
            messagebox.showinfo("Search", "No results found.")
    
    ## Method to delete a contact
    def delete_contact(self):
        selection = self.contact_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        if messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?"):
            del self.contacts[index]
            del self.original_contacts[index]  # Delete from original list
            self.update_contact_listbox()
    
    ## Method to update contact list in ListBox
    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        start_index = (self.page_number - 1) * self.contacts_per_page
        end_index = self.page_number * self.contacts_per_page
        for contact in self.contacts[start_index:end_index]:
            self.contact_listbox.insert(tk.END, " - ".join(contact))
    
    ## Method to export contacts to CSV file
    def export_to_csv(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not filename:
            return
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["First Name", "Last Name", "Phone", "Genre", "Email", "Birthday"])
            for contact in self.contacts:
                writer.writerow(contact)
        messagebox.showinfo("Export to CSV", "Contacts exported successfully.")
    
    ## Method to import contacts from CSV file
    def import_from_csv(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not filename:
            return
        with open(filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            for row in reader:
                self.contacts.append(row)
                self.original_contacts.append(row)  # Add to original list
        self.update_contact_listbox()
    
    ## Method to validate text input
    def validate_text(self, text):
        return all(char.isalpha() or char.isspace() or char in "-'" for char in text)
    
    ## Method to validate phone number input
    def validate_phone(self, phone):
        return all(char.isdigit() or char in "()- " for char in phone)
    
    ## Method to validate email input
    def validate_email(self, email):
        if email == "":
            return True
        return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)
    
    ## Method to clear entry fields
    def clear_fields(self):
        for field, entry in self.entries.items():
            if field != "Genre":
                entry.delete(0, tk.END)
    
    ## Method to view all contacts
    def view_all_contacts(self):
        self.contacts = self.original_contacts[:]
        self.update_contact_listbox()
    
    ## Method for navigating to next page
    def next_page(self):
        total_pages = len(self.original_contacts) // self.contacts_per_page + 1
        if self.page_number < total_pages:
            self.page_number += 1
            self.update_contact_listbox()
    
    ## Method for navigating to previous page
    def previous_page(self):
        if self.page_number > 1:
            self.page_number -= 1
            self.update_contact_listbox()

## Main section
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()