# Import necessary libraries
import random
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

class WordGuessingGame:
    def __init__(self):
        # List of words for the game
        self.word_list = [
            "python", "programming", "computer", "algorithm", 
            "developer", "keyboard", "language", "variable"
        ]
        self.current_word = ""
        self.guessed_letters = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts
        
    # Select a random word from the word list and reset game state
    def select_random_word(self):
        self.current_word = random.choice(self.word_list).lower()
        self.guessed_letters = []
        self.attempts_left = self.max_attempts
        return self.current_word
    
    # Generate a hint by revealing some letters of the word
    # Returns a string with revealed letters and underscores for hidden letters
    def get_hint(self):
        hint = []
        for letter in self.current_word:
            if letter in self.guessed_letters or random.random() < 0.3:  # 30% chance to reveal a letter
                hint.append(letter)
                if letter not in self.guessed_letters:
                    self.guessed_letters.append(letter)
            else:
                hint.append("_")
        return " ".join(hint)
    
    # Check if the user's guess is correct
    # Returns a tuple (is_correct, message)
    def check_guess(self, guess):
        guess = guess.lower().strip()
        
        if not guess.isalpha():
            return (False, "Please enter letters only!")
        
        if len(guess) != len(self.current_word):
            return (False, f"Your guess should be {len(self.current_word)} letters long.")
        
        if guess == self.current_word:
            return (True, "Congratulations! You guessed the word correctly!")
        else:
            self.attempts_left -= 1
            if self.attempts_left <= 0:
                return (False, f"Game over! The word was: {self.current_word}")
            else:
                return (False, f"Incorrect! {self.attempts_left} attempts left. Try again.")

# Play the game in the console
def play_console_version():
    game = WordGuessingGame()
    game.select_random_word()
    
    print("Welcome to Guess the Word Game!")
    print("Try to guess the word based on the hints provided.")
    print(f"The word has {len(game.current_word)} letters.")
    print("Type 'quit' to exit the game.\n")
    
    while game.attempts_left > 0:
        # Show hint
        hint = game.get_hint()
        print(f"\nHint: {hint}")
        
        # Get user input
        guess = input("Your guess: ").strip()
        
        if guess.lower() == "quit":
            print(f"\nGame ended. The word was: {game.current_word}")
            return
        
        # Check the guess
        is_correct, message = game.check_guess(guess)
        print(message)
        
        if is_correct:
            return
    
    # If we get here, the player ran out of attempts
    print("\nBetter luck next time!")

class WordGuessingGUI:
    # GUI version of the word guessing game using Tkinter
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Word Game")
        self.game = WordGuessingGame()
        
        # Game variables
        self.game.select_random_word()
        self.hint_var = StringVar()
        self.message_var = StringVar()
        self.message_var.set(f"Guess the {len(self.game.current_word)}-letter word!")
        
        # Create GUI elements
        self.setup_ui()
        
    # Set up the user interface
    # Hint label
    def setup_ui(self):
        Label(self.root, text="Hint:").pack()
        self.hint_label = Label(self.root, textvariable=self.hint_var, font=("Courier", 14))
        self.hint_label.pack()
        
        # Message label
        self.message_label = Label(self.root, textvariable=self.message_var, fg="blue")
        self.message_label.pack(pady=10)
        
        # Guess entry
        Label(self.root, text="Your guess:").pack()
        self.guess_entry = Entry(self.root, font=("Arial", 12))
        self.guess_entry.pack()
        self.guess_entry.bind("<Return>", lambda event: self.check_guess())
        
        # Buttons
        Button(self.root, text="Get Hint", command=self.show_hint).pack(pady=5)
        Button(self.root, text="Submit Guess", command=self.check_guess).pack(pady=5)
        Button(self.root, text="New Game", command=self.new_game).pack(pady=5)
        
        # Show initial hint
        self.show_hint()
    
    def show_hint(self):
        # Display a new hint to the player
        hint = self.game.get_hint()
        self.hint_var.set(hint)
    
    def check_guess(self):
        # Check the player's guess against the current word
        guess = self.guess_entry.get().strip()
        self.guess_entry.delete(0, 'end')  # Clear the entry field
        
        if not guess:
            return
        
        is_correct, message = self.game.check_guess(guess)
        self.message_var.set(message)
        
        if is_correct:
            self.message_label.config(fg="green")
            self.hint_var.set(self.game.current_word)
        elif self.game.attempts_left <= 0:
            self.message_label.config(fg="red")
            self.hint_var.set(self.game.current_word)
        else:
            self.show_hint()
    
    # Start a new game with a new random word
    def new_game(self):
        self.game.select_random_word()
        self.message_var.set(f"Guess the {len(self.game.current_word)}-letter word!")
        self.message_label.config(fg="blue")
        self.show_hint()

if __name__ == "__main__":
    print("Choose game version:")
    print("1. Console version")
    print("2. GUI version")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        play_console_version()
    elif choice == "2":
        root = Tk()
        app = WordGuessingGUI(root)
        root.mainloop()
    else:
        print("Invalid choice. Please run the program again.")