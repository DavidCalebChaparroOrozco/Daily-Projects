# Function to check if it's safe to color a cell with a given color
def is_safe(board, row, col, color, colors):
    # Check above
    if row > 0 and board[row-1][col] == color:
        return False
    # Check below
    if row < len(board)-1 and board[row+1][col] == color:
        return False
    # Check left
    if col > 0 and board[row][col-1] == color:
        return False
    # Check right
    if col < len(board[0])-1 and board[row][col+1] == color:
        return False
    return True

# Recursive function to try all ways to color the board
def paint_board(board, row, col, colors):
    # If we've reached the end of the column, move to the next row
    if col == len(board[0]):
        col = 0
        row += 1

    # Base case: if we've painted the entire board, print the solution
    if row == len(board):
        print_board(board)
        return

    # Try each color and recursively fill the board
    for color in colors:
        if is_safe(board, row, col, color, colors):
            board[row][col] = color                     # Color the current cell
            paint_board(board, row, col + 1, colors)    # Recur to the next cell
            board[row][col] = None                      # Backtrack (reset the cell)

# Function to print the board
def print_board(board):
    for row in board:
        print(row)
    print()

# Main function to initiate the board coloring
def solve_painting_problem(rows, cols, colors):
    # Initialize an empty board (None means uncolored)
    board = [[None for _ in range(cols)] for _ in range(rows)]
    
    # Start recursive coloring from the top-left corner (row 0, col 0)
    paint_board(board, 0, 0, colors)

# Example usage
if __name__ == "__main__":
    colors = ['Red', 'Green', 'Blue']   # List of available colors
    rows, cols = 3, 3                   # Dimensions of the board (3x3 in this case)
    solve_painting_problem(rows, cols, colors)
