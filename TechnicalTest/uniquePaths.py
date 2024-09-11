class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D array (grid) with dimensions m x n, filled with 1s.
        # This will store the number of ways to reach each cell in the grid.
        dp = [[1] * n for _ in range(m)]
        
        # Iterate over each cell starting from (1, 1) because the first row and first column
        # are always 1 (only one way to reach them: either move right or move down).
        for i in range(1, m):
            for j in range(1, n):
                # For each cell (i, j), the number of ways to reach it is the sum of:
                # 1. The number of ways to reach the cell directly above it (i-1, j).
                # 2. The number of ways to reach the cell directly to the left of it (i, j-1).
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The answer will be in the bottom-right corner of the grid, which is dp[m-1][n-1].
        return dp[m-1][n-1]

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
m1 = 3
n1 = 7
print("Example 1:")
print("Input:", m1)
print("Output:", sol.uniquePaths(m1, n1))
print("=".center(50,"="))

# Example 2
m2 = 3
n2 = 2
print("Example 2:")
print("Input:", m2)
print("Output:", sol.uniquePaths(m2, n2))
print("=".center(50,"="))