from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        m, n = len(grid), len(grid[0])
        
        # Traverse the first row, updating the path sum as only right movement is allowed
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        
        # Traverse the first column, updating the path sum as only down movement is allowed
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        
        # Now, update the rest of the grid. For each cell, choose the minimum sum
        # between coming from the top (downward move) or from the left (right move)
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        # The value at the bottom-right corner will be the minimum path sum
        return grid[m - 1][n - 1]
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
grid1 = [[1,3,1],[1,5,1],[4,2,1]]
print("Example 1:")
print("Input grid1:", grid1 )
print("Output:", sol.minPathSum(grid1))
print("=".center(50,"="))

# Example 2
grid2 = [[1,2,3],[4,5,6]]
print("Example 2:")
print("Input grid2:", grid2)
print("Output:", sol.minPathSum(grid2))
print("=".center(50,"="))
