# Sudoku Solver using recursion and backtracking

# Check if placing num at board[row][col] is valid according to Sudoku rules
def is_valid(board, row, col, num):
    # Check if num exists in the current row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if num exists in the current column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if num exists in the current 3x3 grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

# Solves the Sudoku puzzle using backtracking
def solve_sudoku(board):
    # Find an empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell found
                # Try all possible numbers (1 to 9)
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        # Place num in the cell
                        board[row][col] = num

                        # Recursively attempt to solve the rest of the board
                        if solve_sudoku(board):
                            return True

                        # If placing num doesn't lead to a solution, reset the cell
                        board[row][col] = 0
                
                # If no number can be placed, backtrack
                return False

    # If no empty cell is left, the board is solved
    return True

# Prints the Sudoku board in a readable format
def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)  # Print horizontal separator every 3 rows
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("| ", end="")  # Print vertical separator every 3 columns
            print(board[row][col], end=" ")
        print()

# Example Sudoku board (0 represents an empty cell)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("".center(50,"="))
print("Sudoku Board Before Solving:")
print_board(sudoku_board)

# Solve the Sudoku puzzle
if solve_sudoku(sudoku_board):
    print("".center(50,"="))
    print("\nSudoku Board After Solving:")
    print_board(sudoku_board)
else:
    print("No solution exists for this Sudoku board.")
