# Import necessary libraries
import random

# Game Configuration
GAME_NAME = "Word Raider by David Caleb"
WORD_LIST_FILE = "words.txt"
MAX_TURNS = 5

# Loads words from a file and returns them as a list.
def load_word_bank(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip().lower() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Please provide a valid word list.")
        exit()

# Displays the welcome message with game information.
def display_welcome_message(word_length):
    print(f" Welcome to {GAME_NAME}! ".center(50, "="))
    print(f"The word to guess is {word_length} letters long.")
    print(f"You have {MAX_TURNS} turns to guess the word.")
    print("Good luck!\n")

# Evaluates the user's guess and provides feedback.
def evaluate_guess(guess, selected_word, misplaced_letters, incorrect_letters):
    feedback = []
    for i, letter in enumerate(guess):
        if letter == selected_word[i]:
            # Correct letter in correct position
            feedback.append(letter)  
            misplaced_letters.discard(letter)
        elif letter in selected_word:
            # Correct letter in wrong position
            misplaced_letters.add(letter)  
            feedback.append("_")
        else:
            # Incorrect letter
            incorrect_letters.add(letter)  
            feedback.append("_")
    return " ".join(feedback)

# Main function to run the Word Raider game.
def play_game():
    word_bank = load_word_bank(WORD_LIST_FILE)
    selected_word = random.choice(word_bank)
    word_length = len(selected_word)
    
    incorrect_letters = set()
    misplaced_letters = set()
    used_turns = 0
    
    display_welcome_message(word_length)
    
    while used_turns < MAX_TURNS:
        guess = input("Guess a word (or type 'exit' to quit): ").lower().strip()
        
        if guess == "exit":
            print("Game exited. Thanks for playing!")
            break
        
        if len(guess) != word_length or not guess.isalpha():
            print(f"Invalid input! Please enter a word with {word_length} letters.\n")
            continue
        
        feedback = evaluate_guess(guess, selected_word, misplaced_letters, incorrect_letters)
        print(feedback)
        
        if guess == selected_word:
            print("\nCongratulations! You've guessed the word! 🎉")
            break
        
        used_turns += 1
        
        if used_turns == MAX_TURNS:
            print(f"\nGame over! The correct word was: {selected_word}")
            break
        
        print(f"\nMisplaced letters: {sorted(misplaced_letters)}")
        print(f"Incorrect letters: {sorted(incorrect_letters)}")
        print(f"Used turns: {used_turns}/{MAX_TURNS}\n")

if __name__ == "__main__":
    play_game()
