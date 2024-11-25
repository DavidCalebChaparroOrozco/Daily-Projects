# Importing necessary libraries
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note Taking Application by David Caleb")
        
        # Set dark background color
        self.root.configure(bg="#2E2E2E")

        # List to hold notes
        self.notes = []

        # Create UI components first
        self.create_widgets()

        # Load notes after creating widgets
        self.load_notes()

    def create_widgets(self):
        # Text area for displaying notes with dark background and light text
        self.text_area = tk.Text(self.root, height=15, width=50, bg="#3C3C3C", fg="white", insertbackground='white', font=("Arial", 12))
        self.text_area.pack(pady=10)

        # Frame to hold buttons for better layout
        self.button_frame = tk.Frame(self.root, bg="#2E2E2E")
        self.button_frame.pack(pady=10)

        # Buttons for actions with custom colors
        self.add_button = tk.Button(self.button_frame, text="Add Note", command=self.add_note, bg="#4CAF50", fg="white", font=("Arial", 10))
        self.add_button.grid(row=0, column=0, padx=5)

        self.edit_button = tk.Button(self.button_frame, text="Edit Note", command=self.edit_note, bg="#2196F3", fg="white", font=("Arial", 10))
        self.edit_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Note", command=self.delete_note, bg="#F44336", fg="white", font=("Arial", 10))
        self.delete_button.grid(row=0, column=2, padx=5)

        self.search_button = tk.Button(self.button_frame, text="Search Note", command=self.search_note, bg="#FF9800", fg="white", font=("Arial", 10))
        self.search_button.grid(row=0, column=3, padx=5)

    # Load notes from a JSON file.
    def load_notes(self):
        if os.path.exists("notes.json"):
            with open("notes.json", "r") as file:
                self.notes = json.load(file)
            self.update_text_area()

    # Save notes to a JSON file.
    def save_notes(self):
        with open("notes.json", "w") as file:
            json.dump(self.notes, file)

    def add_note(self):
        note = simpledialog.askstring("New Note", "Enter your note:")
        if note:
            self.notes.append(note)
            self.save_notes()
            self.update_text_area()

    def edit_note(self):
        index = simpledialog.askinteger("Edit Note", "Enter note index to edit (0-based):")
        if index is not None and 0 <= index < len(self.notes):
            new_note = simpledialog.askstring("Edit Note", "Enter your new note:", initialvalue=self.notes[index])
            if new_note:
                self.notes[index] = new_note
                self.save_notes()
                self.update_text_area()
        else:
            messagebox.showerror("Error", "Invalid index!")

    def delete_note(self):
        index = simpledialog.askinteger("Delete Note", "Enter note index to delete (0-based):")
        if index is not None and 0 <= index < len(self.notes):
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this note?"):
                del self.notes[index]
                self.save_notes()
                self.update_text_area()
        else:
            messagebox.showerror("Error", "Invalid index!")

    def search_note(self):
        search_term = simpledialog.askstring("Search Note", "Enter search term:")
        if search_term:
            results = [note for note in self.notes if search_term in note]
            if results:
                messagebox.showinfo("Search Results", "\n".join(results))
            else:
                messagebox.showinfo("Search Results", "No notes found.")

    # Update the text area with current notes.
    def update_text_area(self):
        self.text_area.delete(1.0, tk.END)  # Clear the text area
        for i, note in enumerate(self.notes):
            self.text_area.insert(tk.END, f"{i}: {note}\n")  # Display notes with their indices

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()