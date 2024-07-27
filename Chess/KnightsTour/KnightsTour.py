# Board dimensions
N = 8

# Possible knight moves
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

# Function to check if a position is valid
def is_valid(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(str(cell).zfill(2) for cell in row))
    print()

# Recursive function to solve the knight's tour problem
def knight_tour(x, y, move_num, board):
    if move_num == N * N:
        return True

    for i in range(8):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if is_valid(new_x, new_y, board):
            board[new_x][new_y] = move_num
            if knight_tour(new_x, new_y, move_num + 1, board):
                return True
            board[new_x][new_y] = -1  # Backtracking

    return False

# Main function to start the knight's tour
def solve_knight_tour():
    board = [[-1 for _ in range(N)] for _ in range(N)]
    # Start from the top-left corner
    board[0][0] = 0

    if not knight_tour(0, 0, 1, board):
        print("No solution")
    else:
        print("Board with the knight's journey:")
        print_board(board)

# Run the program
if __name__ == "__main__":
    solve_knight_tour()