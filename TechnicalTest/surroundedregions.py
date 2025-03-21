from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        rows, cols = len(board), len(board[0])
        
        # Traverse the borders and mark 'O's and their connected regions as safe (using 'T')
        def dfs(row, col):
            # Base case: If out of bounds or not 'O', return
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != 'O':
                return
            # Mark the current cell as safe
            board[row][col] = 'T'
            # Recursively visit all adjacent cells
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        # Traverse the first and last rows
        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)
        
        # Traverse the first and last columns
        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)
        
        # Replace all remaining 'O's with 'X's (capture surrounded regions)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        
        # Restore the safe 'O's (marked as 'T') back to 'O'
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'T':
                    board[row][col] = 'O'

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
board1 = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
print("Example 1:")
print("Input:")
for row in board1:
    print(row)
sol.solve(board1)  
print("Output:")
for row in board1:
    print(row)
print("=".center(50, "="))

# Example 2
board2 = [["X"]]
print("Example 2:")
print("Input:")
for row in board2:
    print(row)
sol.solve(board2)  
print("Output:")
for row in board2:
    print(row)
print("=".center(50, "="))