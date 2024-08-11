# Importing necessary libraries
from flask import Flask, render_template, request, session, redirect, url_for
import random
import os
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

# Retrieving key from environment variables
KEY = os.getenv("SECRET_KEY")

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = KEY

# Load words from the words.txt file
with open('words.txt') as f:
    words = [word.strip().lower() for word in f.readlines()]

@app.route('/', methods=['GET', 'POST'])
def index():
    # Check if a word is already in the session; if not, start a new game
    if 'word' not in session:
        session['word'] = random.choice(words)
        session['attempts'] = []
        session['won'] = False
        session['game_over'] = False

    attempts = session.get('attempts', [])

    # Handle the form submission for a new guess
    if request.method == 'POST' and not session.get('game_over', False):
        guess = request.form.get('guess').lower()
        
        # Validate the guess: it must be a 5-letter word from the list
        if len(guess) == 5 and guess in words:
            feedback = []
            word = session['word']
            
            # Compare the guess with the correct word
            for i, letter in enumerate(guess):
                if letter == word[i]:
                    feedback.append('correct')
                elif letter in word:
                    feedback.append('present')
                else:
                    feedback.append('absent')

            # Store the attempt with feedback
            attempts.append({'guess': guess, 'feedback': feedback})
            session['attempts'] = attempts

            if guess == word:
                session['won'] = True
        else:
            session['error'] = "Please enter a valid 5-letter word."

    # Check if the maximum number of attempts has been reached
    if len(attempts) >= 8 and not session.get('won', False):
        session['game_over'] = True
        session['error'] = f"Game over! The correct word was '{session['word']}'." 

    # Retrieve and clear the error message from the session
    error_message = session.pop('error', None)
    
    return render_template('index.html', attempts=attempts, won=session.get('won', False), error=error_message, game_over=session.get('game_over', False), correct_word=session.get('word'))

@app.route('/restart')
def restart():
    # Reset the game state by clearing the session variables
    session.pop('word', None)
    session.pop('attempts', None)
    session.pop('won', None)
    session.pop('game_over', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
