# Import necessary libraries
from spellchecker import SpellChecker  
import tkinter as tk  
from tkinter import messagebox, scrolledtext  

# Create a class for the Spell Checker Application
class SpellCheckerApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Simple Spell Checker by David Caleb")  
        self.root.geometry("600x600")  
        self.root.configure(bg="#2E3440")  

        # Initialize the spell checker
        self.spell = SpellChecker()

        # List to store history of checked words
        self.history = []

        # Create and place the widgets
        self.create_widgets()

    def create_widgets(self):
        # Configure styles for dark theme
        self.label_style = {"font": ("Arial", 12), "bg": "#2E3440", "fg": "#D8DEE9"}
        self.entry_style = {"font": ("Arial", 12), "bg": "#4C566A", "fg": "#ECEFF4", "insertbackground": "white"}
        self.button_style = {"font": ("Arial", 12), "bg": "#5E81AC", "fg": "#ECEFF4", "activebackground": "#81A1C1"}
        self.result_style = {"font": ("Arial", 12), "bg": "#2E3440", "fg": "#88C0D0"}
        self.history_style = {"font": ("Arial", 10), "bg": "#3B4252", "fg": "#ECEFF4"}

        # Label for instructions
        self.label = tk.Label(self.root, text="Enter a word to check its spelling:", **self.label_style)
        self.label.pack(pady=10)

        # Entry widget for user input
        self.entry = tk.Entry(self.root, **self.entry_style, width=30)
        self.entry.pack(pady=10)

        # Frame to hold buttons
        self.button_frame = tk.Frame(self.root, bg="#2E3440")
        self.button_frame.pack(pady=10)

        # Button to trigger spell checking
        self.check_button = tk.Button(self.button_frame, text="Check Spelling", **self.button_style, command=self.check_spelling)
        self.check_button.pack(side=tk.LEFT, padx=5)

        # Button to clear input and results
        self.clear_button = tk.Button(self.button_frame, text="Clear", **self.button_style, command=self.clear_input)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Label to display the result
        self.result_label = tk.Label(self.root, text="", **self.result_style)
        self.result_label.pack(pady=20)

        # Label for history section
        self.history_label = tk.Label(self.root, text="History of Checked Words:", **self.label_style)
        self.history_label.pack(pady=10)

        # Scrollable text area to display history
        self.history_text = scrolledtext.ScrolledText(self.root, **self.history_style, width=50, height=10, state="disabled")
        self.history_text.pack(pady=10)

    def check_spelling(self):
        # Get the word from the entry widget
        word = self.entry.get().strip()

        # Check if the word is empty
        if not word:
            messagebox.showwarning("Input Error", "Please enter a word to check.", parent=self.root)
            return

        # Check if the word is spelled correctly
        if word in self.spell:
            self.result_label.config(text=f"'{word}' is spelled correctly!", fg="#A3BE8C")  # Green for correct
        else:
            # Get the most likely correct spelling
            corrected_word = self.spell.correction(word)
            # Get a list of possible corrections
            suggestions = self.spell.candidates(word)

            # Display the result
            self.result_label.config(
                text=f"Did you mean '{corrected_word}'?\nSuggestions: {', '.join(suggestions)}",
                fg="#BF616A"
            )

        # Add the word to history
        self.history.append(word)
        self.update_history()

    def clear_input(self):
        # Clear the entry widget and result label
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.history_text.config(state="normal")
        self.history_text.delete(1.0, tk.END)
        self.history_text.config(state="disabled")

    def update_history(self):
        # Update the history text area with the list of checked words
        self.history_text.config(state="normal")
        self.history_text.delete(1.0, tk.END)
        for word in self.history:
            self.history_text.insert(tk.END, f"- {word}\n")
        self.history_text.config(state="disabled")

# Main function to run the application
def main():
    # Create the root window
    root = tk.Tk()
    # Create an instance of the SpellCheckerApp
    app = SpellCheckerApp(root)
    # Run the application
    root.mainloop()

# Entry point of the program
if __name__ == "__main__":
    main()