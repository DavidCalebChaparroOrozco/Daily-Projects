# Importing necessary libraries
import tkinter as tk
from tkinter import messagebox, simpledialog

# Flashcard class to represent individual flashcards
class Flashcard:
    def __init__(self, front, back):
        # Question or term
        self.front = front  
        # Answer or definition
        self.back = back    

# FlashcardManager class to handle flashcard operations
class FlashcardManager:
    def __init__(self):
        # List to store flashcards
        self.flashcards = []  
        self.current_card_index = 0
        # User's score in quiz mode
        self.score = 0  

    # Add a new flashcard
    def add_flashcard(self, front, back):
        card = Flashcard(front, back)
        self.flashcards.append(card)

    # Edit an existing flashcard
    def edit_flashcard(self, index, new_front, new_back):
        if 0 <= index < len(self.flashcards):
            self.flashcards[index].front = new_front
            self.flashcards[index].back = new_back

    # Get the current flashcard
    def get_current_flashcard(self):
        if len(self.flashcards) > 0:
            return self.flashcards[self.current_card_index]
        return None

    # Go to the next flashcard
    def next_flashcard(self):
        if len(self.flashcards) > 0:
            self.current_card_index = (self.current_card_index + 1) % len(self.flashcards)

    # Go to the previous flashcard
    def previous_flashcard(self):
        if len(self.flashcards) > 0:
            self.current_card_index = (self.current_card_index - 1) % len(self.flashcards)

    # Reset quiz mode
    def reset_quiz(self):
        self.score = 0
        self.current_card_index = 0

    # Check answer and update score
    def check_answer(self, user_answer):
        current_card = self.get_current_flashcard()
        if current_card and user_answer.strip().lower() == current_card.back.strip().lower():
            self.score += 1
            return True
        return False

# FlashcardApp class to build the GUI
class FlashcardApp:
    def __init__(self, root):
        self.manager = FlashcardManager()  # Flashcard manager instance

        # Set up the main window
        self.root = root
        self.root.title("Flashcard Creator by David Caleb")
        self.root.geometry("500x400")

        # Create the main widgets
        self.front_label = tk.Label(root, text="Front: ", font=("Arial", 14))
        self.front_label.pack(pady=10)

        self.front_text = tk.Text(root, height=2, width=30)
        self.front_text.pack(pady=5)

        self.back_label = tk.Label(root, text="Back: ", font=("Arial", 14))
        self.back_label.pack(pady=10)

        self.back_text = tk.Text(root, height=2, width=30)
        self.back_text.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Flashcard", command=self.add_flashcard)
        self.add_button.pack(pady=10)

        self.edit_button = tk.Button(root, text="Edit Current Flashcard", command=self.edit_flashcard)
        self.edit_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next Flashcard", command=self.next_flashcard)
        self.next_button.pack(pady=5)

        self.previous_button = tk.Button(root, text="Previous Flashcard", command=self.previous_flashcard)
        self.previous_button.pack(pady=5)

        self.quiz_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.quiz_button.pack(pady=10)

        self.status_label = tk.Label(root, text="", font=("Arial", 12))
        self.status_label.pack(pady=20)

    # Add a flashcard to the manager
    def add_flashcard(self):
        front = self.front_text.get("1.0", tk.END).strip()
        back = self.back_text.get("1.0", tk.END).strip()

        if front and back:
            self.manager.add_flashcard(front, back)
            messagebox.showinfo("Success", "Flashcard added successfully!")
            self.clear_fields()
        else:
            messagebox.showwarning("Warning", "Please fill out both fields.")

    # Edit the current flashcard
    def edit_flashcard(self):
        current_card = self.manager.get_current_flashcard()

        if current_card:
            front = self.front_text.get("1.0", tk.END).strip()
            back = self.back_text.get("1.0", tk.END).strip()
            self.manager.edit_flashcard(self.manager.current_card_index, front, back)
            messagebox.showinfo("Success", "Flashcard edited successfully!")
            self.clear_fields()
        else:
            messagebox.showwarning("Warning", "No flashcard to edit.")

    # Show the next flashcard in the sequence
    def next_flashcard(self):
        self.manager.next_flashcard()
        self.display_current_flashcard()

    # Show the previous flashcard in the sequence
    def previous_flashcard(self):
        self.manager.previous_flashcard()
        self.display_current_flashcard()

    # Display the current flashcard on the screen
    def display_current_flashcard(self):
        current_card = self.manager.get_current_flashcard()

        if current_card:
            self.front_text.delete("1.0", tk.END)
            self.front_text.insert(tk.END, current_card.front)

            self.back_text.delete("1.0", tk.END)
            self.back_text.insert(tk.END, current_card.back)
        else:
            self.status_label.config(text="No flashcards available")

    # Start the quiz mode
    def start_quiz(self):
        self.manager.reset_quiz()
        self.quiz_round()

    # Quiz round logic
    def quiz_round(self):
        current_card = self.manager.get_current_flashcard()

        if current_card:
            user_answer = simpledialog.askstring("Quiz", f"Question: {current_card.front}")
            if user_answer is not None:
                if self.manager.check_answer(user_answer):
                    messagebox.showinfo("Correct!", "Correct answer!")
                else:
                    messagebox.showwarning("Incorrect", f"Incorrect! The correct answer is {current_card.back}")
            self.manager.next_flashcard()

            if self.manager.current_card_index == 0:
                messagebox.showinfo("Quiz Finished", f"Quiz finished! Your score: {self.manager.score}")
            else:
                self.quiz_round()
        else:
            messagebox.showinfo("No Cards", "No flashcards to quiz.")

    # Clear the text fields after adding or editing flashcards
    def clear_fields(self):
        self.front_text.delete("1.0", tk.END)
        self.back_text.delete("1.0", tk.END)

# Main application execution
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
