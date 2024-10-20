from typing import List

class Solution:
    def WordSearch(self, board: List[List[str]], word: str) -> bool:
        # Function to perform Depth-First Search (DFS) from a starting point (i, j)
        def dfs(i: int, j: int, k: int) -> bool:
            # If all characters of the word have been matched, return True
            if k == len(word):
                return True
            # Check if the current cell is out of bounds or doesn't match the current character of the word
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            
            # Temporarily mark the current cell as visited by setting it to a placeholder
            temp = board[i][j]
            board[i][j] = '#'
            
            # Explore all four possible directions: up, down, left, right
            found = (dfs(i + 1, j, k + 1) or  # Move down
                    dfs(i - 1, j, k + 1) or  # Move up
                    dfs(i, j + 1, k + 1) or  # Move right
                    dfs(i, j - 1, k + 1))    # Move left
            
            # Restore the current cell back to its original state after exploring
            board[i][j] = temp
            
            return found
        
        # Start DFS from every cell in the board to check if the word can be formed
        for i in range(len(board)):
            for j in range(len(board[0])):
                # If DFS from a starting point returns True, the word exists in the grid
                if dfs(i, j, 0):
                    return True
        
        # If no valid path is found, return False
        return False

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
print("Example 1:")
print("Input:", board1)
print("Output:",sol.WordSearch(board1, word1))
print("=".center(50, "="))

# Example 2
board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"
print("Example 2:")
print("Input:", board2)
print("Output:",sol.WordSearch(board2, word2))
print("=".center(50, "="))

# Example 3
board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word3 = "ABCB"
print("Example 3:")
print("Input:", board3)
print("Output:",sol.WordSearch(board3, word3))
print("=".center(50, "="))