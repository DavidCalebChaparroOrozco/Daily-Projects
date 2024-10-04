# Importing necessary libraries
import numpy as np

# Define a function to convert FEN notation to a chess board (8x8 matrix)
def fen_to_board(fen):
    # Split the FEN string to get the board layout
    fen_board = fen.split(' ')[0]
    
    # Create an empty 8x8 board
    board = []
    
    # Rows in FEN are separated by '/', so split the rows
    for row in fen_board.split('/'):
        board_row = []
        
        # Loop through each character in the row
        for char in row:
            if char.isdigit():
                # If it's a digit, add that many empty spaces to the row
                board_row.extend(['.'] * int(char))
            else:
                # Otherwise, add the piece symbol to the row
                board_row.append(char)
        
        # Append the row to the board
        board.append(board_row)
    
    # Convert the board to a NumPy array for better visualization and return it
    return np.array(board)

# Function to convert a board (8x8 matrix) back to FEN notation
def board_to_fen(board):
    # Create an empty list to store FEN rows
    fen_rows = []
    
    # Iterate over each row in the board
    for row in board:
        empty_count = 0
        fen_row = ""
        
        for square in row:
            if square == '.':
                # Count empty squares
                empty_count += 1
            else:
                # If there's a piece, add the number of empty squares (if any) first
                if empty_count > 0:
                    fen_row += str(empty_count)
                    empty_count = 0
                # Add the piece symbol
                fen_row += square
        
        # If the row ends with empty squares, add the count
        if empty_count > 0:
            fen_row += str(empty_count)
        
        # Append the processed row to the list
        fen_rows.append(fen_row)
    
    # Join the rows with '/' and add additional fields for a complete FEN string
    return '/'.join(fen_rows) + ' w KQkq - 0 1'

# Function to display the board visually in the console
def print_board(board):
    # Iterate over each row and print it
    for row in board:
        print(' '.join(row))
    print()

# Sample FEN notation (this represents the starting position in chess)
sample_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

# Convert FEN to board
chess_board = fen_to_board(sample_fen)

# Print the board
print("Chess board from FEN:")
print_board(chess_board)

# Convert the board back to FEN
fen_from_board = board_to_fen(chess_board)

# Print the FEN notation from the board
print("FEN notation from the board:")
print(fen_from_board)