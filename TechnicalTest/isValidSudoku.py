# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according 
# to the following rules:
#   - Each row must contain the digits 1-9 without repetition.
#   - Each column must contain the digits 1-9 without repetition.
#   - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without 
#     repetition.
# Note:
#  A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#  Only the filled cells need to be validated according to the mentioned rules.

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to keep track of seen numbers in rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                
                # Check row
                if num in rows[r]:
                    return False
                rows[r].add(num)
                
                # Check column
                if num in cols[c]:
                    return False
                cols[c].add(num)
                
                # Check 3x3 box
                box_index = (r // 3) * 3 + (c // 3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        
        return True

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print("Example 1:", sol.isValidSudoku(board1))
print("=".center(50,"="))

# Example 2
board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print("Example 2:", sol.isValidSudoku(board2))  
print("=".center(50,"="))