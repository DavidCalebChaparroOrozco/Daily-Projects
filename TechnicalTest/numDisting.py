class Solution:
    # Return the number of distinct subsequences of s which equals t.
    def numDistinct(self, s: str, t: str) -> int:
        """    
        s: The source string
        t: The target string
        return: The number of distinct subsequences of s that equal t
        """
        # Lengths of the input strings
        m, n = len(s), len(t)
        
        # Create a 2D DP array with (m+1) x (n+1) dimensions
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # An empty string t can be formed by any prefix of s (including empty prefix)
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match, we can either include this character or exclude it
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # If characters do not match, we can only exclude the character from s
                    dp[i][j] = dp[i - 1][j]
        
        # The bottom-right cell contains the answer
        return dp[m][n]

# Example usage
sol = Solution()

# Example 1
s1 = "rabbbit"
t1 = "rabbit"
output1 = sol.numDistinct(s1, t1)
print("Example 1:")
print(f"Input: s = '{s1}', t = '{t1}'")
print(f"Output: {output1}")  

# Example 2
s2 = "babgbag"
t2 = "bag"
output2 = sol.numDistinct(s2, t2)
print("Example 2:")
print(f"\nInput: s = '{s2}', t = '{t2}'")
print(f"Output: {output2}")  

# Example 3
s3 = "aaa"
t3 = "aa"
output3 = sol.numDistinct(s3, t3)
print("Example 3:")
print(f"\nInput: s = '{s3}', t = '{t3}'")
print(f"Output: {output3}")  
