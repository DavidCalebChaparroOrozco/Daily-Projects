from typing import List

class Solution:
    # Do not return anything, modify board in-place instead.
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(board: List[List[str]], row: int, col: int, num: str) -> bool:
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            return True
        
        def solve(board: List[List[str]]) -> bool:
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in '123456789':
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if solve(board):
                                    return True
                                board[row][col] = '.'
                        return False
            return True
        
        solve(board)

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

# Solve the Sudoku
sol.solveSudoku(board1)

# Print the solved board
print("Example 1 Solved Board:")
for row in board1:
    print(row)
print("=".center(50,"="))