# Importing necessary libraries
from random import randint

# Dictionary to map letters to numbers for column indices
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

# Function to create ships on the hidden board
def create_ships(board):
    for _ in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "X"

# Function to count the number of hits on the guess board
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count
