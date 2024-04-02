# Importing necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import random
import re

# Creating a Flask application instance
app = Flask(__name__)

# Opening the file containing words
with open('words.txt', 'r') as file:
    words = file.readlines()

# Function to get a random word
def get_random_word():
    return random.choice(words).strip().upper()

# Function to generate the display of the word with guessed letters
def get_word_display(word, guesses):
    return ' '.join(letter if letter in guesses else '_' for letter in word)

# Function to check if a guess is valid
def is_valid_guess(guess):
    return re.match("^[a-zA-Z]$", guess) is not None

# Route for the main Hangman game
@app.route('/', methods=['GET', 'POST'])
def hangman():
    error_message = ''
    if request.method == 'GET':
        word = get_random_word()
        guesses = set()
        allowed_errors = 7
    elif request.method == 'POST':
        word = request.form['word']
        guesses = set(request.form['guesses'])
        allowed_errors = int(request.form['allowed_errors'])
        guess = request.form['guess'].upper()

        # Validating the guess
        if guess == '' or guess.isspace():
            error_message = 'Please enter a letter.'
        elif not is_valid_guess(guess):
            error_message = 'Please enter a letter.'
        elif guess in guesses:
            error_message = 'You have already tried this letter.'
        else:
            guesses.add(guess)

            # Checking if the guess is incorrect
            if guess not in word:
                allowed_errors -= 1

    # Generating the display of the word with guessed letters
    word_display = get_word_display(word, guesses)

    # Checking if the game is over
    game_over = allowed_errors == 0 or all(letter in guesses for letter in word)

    # Rendering the Hangman template with appropriate variables
    if game_over:
        return render_template('hangman.html', word_display=word, guesses=guesses, allowed_errors=allowed_errors, game_over=game_over, word=word)
    return render_template('hangman.html', word_display=word_display, guesses=guesses, allowed_errors=allowed_errors, game_over=game_over, word=word, error_message=error_message)

# Route for retrying the game
@app.route('/retry', methods=['GET'])
def retry():
    return redirect(url_for('hangman'))

# Running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
