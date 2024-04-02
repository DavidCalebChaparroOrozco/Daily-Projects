# Importing necessary libraries
import random

# Opening the file containing words
with open('words.txt', 'r') as file:
    # Reading lines from the file
    word = file.readlines()
    
# Choosing a random word from the list
word = random.choice(word)[:-1]

# Setting the maximum allowed errors
allowed_errors = 7

# List to store guessed letters
guesses = []

# Flag to check if the game is done
done = False

# Main game loop
while not done:
    # Displaying the current state of the word
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    # Getting the next guess from the user
    guess = input(f"Allowed Errors Left: {allowed_errors}, Next Guess: ")
    guesses.append(guess.lower())
    
    # Checking if the guess is correct
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    # Checking if all letters have been guessed
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

# Displaying the result of the game
if done:
    print(f"You found the word! It was {word}!")
else:
    print(f"Game Over! The word was {word}!")
