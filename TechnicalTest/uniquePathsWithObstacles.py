class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # Get the dimensions of the grid (m rows and n columns)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If the start or end point has an obstacle, no path is possible.
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        # Initialize a 2D array (dp) to store the number of ways to reach each cell.
        # Initialize all cells with 0 by default.
        dp = [[0] * n for _ in range(m)]
        
        # Set the starting point (top-left corner) to 1 if there's no obstacle.
        dp[0][0] = 1
        
        # Fill the first row: a cell can be reached if there's no obstacle
        # and the previous cell (to the left) can be reached.
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        
        # Fill the first column: a cell can be reached if there's no obstacle
        # and the cell above it can be reached.
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        # Iterate over the rest of the grid starting from (1, 1).
        for i in range(1, m):
            for j in range(1, n):
                # Only process cells that are not obstacles.
                if obstacleGrid[i][j] == 0:
                    # A cell (i, j) can be reached either from the top (i-1, j) or
                    # from the left (i, j-1), but only if those cells are reachable.
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The answer will be in the bottom-right corner of the grid.
        return dp[m-1][n-1]

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
obstacleGrid1 = [[0,0,0],[0,1,0],[0,0,0]]
print("Example 1:")
print("Input:", obstacleGrid1)
print("Output:", sol.uniquePathsWithObstacles(obstacleGrid1))
print("=".center(50,"="))

# Example 2
obstacleGrid2 = [[0,1],[0,0]]
print("Example 2:")
print("Input:", obstacleGrid2)
print("Output:", sol.uniquePathsWithObstacles(obstacleGrid2))
print("=".center(50,"="))