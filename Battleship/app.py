# Importing necessary libraries
from flask import Flask, render_template, request, redirect, url_for, session
from battleship import create_ships, count_hit_ships, letters_to_numbers
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    # Initialize the hidden and guess boards
    session['HIDDEN_BOARD'] = [[" "] * 8 for _ in range(8)]
    session['GUESS_BOARD'] = [[" "] * 8 for _ in range(8)]
    create_ships(session['HIDDEN_BOARD'])
    session['turns'] = 10
    return redirect(url_for('game'))

@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'GUESS_BOARD' not in session or 'HIDDEN_BOARD' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        row = int(request.form['row']) - 1
        column = letters_to_numbers[request.form['column'].upper()]
        guess_board = session['GUESS_BOARD']
        hidden_board = session['HIDDEN_BOARD']
        turns = session['turns']

        if guess_board[row][column] == "-":
            message = "You guessed that one already."
        elif hidden_board[row][column] == "X":
            message = "Hit"
            guess_board[row][column] = "X"
            turns -= 1
        else:
            message = "MISS!"
            guess_board[row][column] = "-"
            turns -= 1

        session['GUESS_BOARD'] = guess_board
        session['turns'] = turns

        if count_hit_ships(guess_board) == 5:
            return render_template('game.html', guess_board=guess_board, message="You win!", game_over=True)
        elif turns == 0:
            # Show all ship locations if the game is over
            for r in range(8):
                for c in range(8):
                    if hidden_board[r][c] == "X":
                        guess_board[r][c] = "O" if guess_board[r][c] != "X" else "X"
            return render_template('game.html', guess_board=guess_board, message="You ran out of turns", game_over=True)

        return render_template('game.html', guess_board=guess_board, message=message, game_over=False, turns=turns)

    return render_template('game.html', guess_board=session['GUESS_BOARD'], game_over=False, turns=session['turns'])

if __name__ == "__main__":
    app.run(debug=True)