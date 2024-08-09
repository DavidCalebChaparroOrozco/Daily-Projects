from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_not_under_attack(row, col):
            # Check if any queen can attack the position (row, col)
            return not (cols[col] or hills[row - col] or dales[row + col])

        def place_queen(row, col):
            # Place a queen on the board at (row, col)
            queens[row] = col
            cols[col] = 1
            hills[row - col] = 1  # "hill" diagonals
            dales[row + col] = 1  # "dale" diagonals

        def remove_queen(row, col):
            # Remove a queen from the board at (row, col)
            queens[row] = -1
            cols[col] = 0
            hills[row - col] = 0
            dales[row + col] = 0

        def add_solution():
            # Construct a solution from the current board state
            solution = []
            for i in range(n):
                row = ['.'] * n
                row[queens[i]] = 'Q'
                solution.append("".join(row))
            output.append(solution)

        def backtrack(row = 0):
            # Try placing a queen in every column in the current row
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    # If all queens are placed successfully, add the solution
                    if row + 1 == n:
                        add_solution()
                    else:
                        # Move on to the next row
                        backtrack(row + 1)
                    # Backtrack: Remove the queen and try the next column
                    remove_queen(row, col)

        # Initialize data structures
        # Columns
        cols = [0] * n  
        # "hill" diagonals
        hills = [0] * (2 * n - 1)  
        # "dale" diagonals
        dales = [0] * (2 * n - 1)  
        # Queen positions
        queens = [-1] * n  
        output = []

        # Start the backtracking process from the first row
        backtrack()
        return output

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
n1 = 4
print("Example 1:")
print("Input:", n1)
print("Output:", sol.solveNQueens(n1))
print("=".center(50,"="))

# Example 2
n2 = 1
print("Example 2:")
print("Input:", n2)
print("Output:", sol.solveNQueens(n2))
print("=".center(50,"="))
