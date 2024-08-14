class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(row, col):
            # Check if there's any queen in the same column, or in the diagonals
            return not (cols[col] or hill_diagonals[row - col] or dale_diagonals[row + col])

        def place_queen(row, col):
            # Place a queen on the board and mark the attacked columns and diagonals
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1

        def remove_queen(row, col):
            # Remove a queen from the board and unmark the attacked columns and diagonals
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0

        def backtrack(row=0, count=0):
            # Start the backtracking process
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        # If all queens are placed, increment the solution count
                        count += 1
                    else:
                        # Proceed to place the next queen
                        count = backtrack(row + 1, count)
                    remove_queen(row, col)
            return count

        # Initialize arrays to keep track of attacked columns and diagonals
        cols = [0] * n
        # from -(n-1) to n-1
        hill_diagonals = [0] * (2 * n - 1)  
        # from 0 to 2n-2
        dale_diagonals = [0] * (2 * n - 1)  

        # Start the backtracking from the first row
        return backtrack()

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
n1 = 4
print("Example 1:")
print("Input:", n1)
print("Output:", sol.totalNQueens(n1))
print("=".center(50,"="))

# Example 2
n2 = 1
print("Example 2:")
print("Input:", n2)
print("Output:", sol.totalNQueens(n2))
print("=".center(50,"="))
