class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Get the lengths of both words
        len1 = len(word1)
        len2 = len(word2)
        
        # Create a 2D table to store the minimum number of operations
        # dp[i][j] will hold the minimum number of operations required
        # to convert word1[0..i-1] to word2[0..j-1]
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        
        # Fill the first row and column of the dp table
        # The first row represents converting an empty word1 to word2
        # The first column represents converting word1 to an empty word2
        for i in range(len1 + 1):
            dp[i][0] = i  # i deletions
        for j in range(len2 + 1):
            dp[0][j] = j  # j insertions
        
        # Compute the dp values for the rest of the table
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # If the characters are the same, no change is needed
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Find the minimum cost between insertion, deletion, or replacement
                    dp[i][j] = 1 + min(dp[i - 1][j],    # Deletion
                                    dp[i][j - 1],       # Insertion
                                    dp[i - 1][j - 1])   # Replacement
        
        # The final result is in the bottom-right corner of the table
        return dp[len1][len2]

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
word1 = "horse"
word2 = "ros"
print("Example 1:")
print("Input:", word1)
print("Output:", sol.minDistance(word1, word2))
print("=".center(50,"="))

# Example 2
word3 = "intention"
word4 = "execution"
print("Example 1:")
print("Input:", word3)
print("Output:", sol.minDistance(word3, word4))
print("=".center(50,"="))