from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Initialize game board
def initialize_game():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

# Add a new tile to the board
def add_new_tile(board):
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if not empty_tiles:
        return
    i, j = random.choice(empty_tiles)
    board[i][j] = 2 if random.random() < 0.9 else 4

# Move tiles to the left
def move_left(board):
    new_board = []
    for row in board:
        new_row = [num for num in row if num != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [num for num in new_row if num != 0]
        new_board.append(new_row + [0] * (4 - len(new_row)))
    return new_board

# Transpose the board for moving up/down
def transpose(board):
    return [list(row) for row in zip(*board)]

# Reverse the board for moving right
def reverse(board):
    return [row[::-1] for row in board]

# Perform a move based on direction
def move(board, direction):
    if direction == 'left':
        return move_left(board)
    elif direction == 'right':
        return reverse(move_left(reverse(board)))
    elif direction == 'up':
        return transpose(move_left(transpose(board)))
    elif direction == 'down':
        return transpose(reverse(move_left(reverse(transpose(board)))))

# Check if the game is over
def is_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
    return True

# Autoplay function
def autoplay(board):
    directions = ['left', 'right', 'up', 'down']
    while not is_game_over(board):
        direction = random.choice(directions)
        new_board = move(board, direction)
        if new_board != board:
            board = new_board
            add_new_tile(board)
    return board

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    board = initialize_game()
    return jsonify(board=board)

@app.route('/move', methods=['POST'])
def move_tile():
    data = request.get_json()
    direction = data['direction']
    board = data['board']
    new_board = move(board, direction)
    if new_board != board:
        add_new_tile(new_board)
    return jsonify(board=new_board, game_over=is_game_over(new_board))

@app.route('/autoplay', methods=['POST'])
def autoplay_game():
    data = request.get_json()
    board = data['board']
    final_board = autoplay(board)
    return jsonify(board=final_board)

if __name__ == '__main__':
    app.run(debug=True)
