class Solution:
    def numTrees(self, n: int) -> int:
        # Initialize a list to store the number of unique BSTs for each count of nodes
        dp = [0] * (n + 1)
        
        # Base case: There is one unique BST for 0 nodes and one for 1 node
        dp[0], dp[1] = 1, 1
        
        # Fill the dp array using the formula:
        # dp[i] = sum(dp[j] * dp[i - 1 - j]) for j in range(i)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        
        # The result for n nodes is stored in dp[n]
        return dp[n]
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
n1 = 3
print("Example 1:")
print("Input:", n1)
print("Output:", sol.numTrees(n1))
print("=".center(50,"="))

# Example 2
n2 = 1
print("Example 2:")
print("Input:", n2)
print("Output:", sol.numTrees(n2))
print("=".center(50,"="))