# Function to check if a position on the board is safe for a queen.
def is_safe(board, row, col):
    # Check if there is a queen in the same column.
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check if there is a queen in the upper diagonal.
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check if there is a queen in the lower diagonal.
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

# Function to solve the N Queens problem using backtracking.
def solve_n_queens_util(board, col):
    # Base case: if all columns have been filled, return True.
    if col >= len(board):
        return True
    # Try to place a queen in each row.
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            # Recursively try to place queens in the next column.
            if solve_n_queens_util(board, col + 1):
                return True
            # If the placement does not lead to a solution, backtrack.
            board[i][col] = 0
    return False

# Function to solve the N Queens problem.
def solve_n_queens(n):
    # Initialize the board with zeros.
    board = [[0] * n for _ in range(n)]
    # Try to place queens on the board.
    if not solve_n_queens_util(board, 0):
        print("There is no solution")
        return
    # Print the solution.
    for row in board:
        print(row)

# Example of use:
solve_n_queens(7)
