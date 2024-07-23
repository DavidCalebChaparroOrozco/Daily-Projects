# Given an input string (s) and a pattern (p), implement wildcard pattern matching with 
# support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] will be True if the first i characters in s match the first j characters in p
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Both the empty string and empty pattern match
        dp[0][0] = True
        
        # Only '*' can match with an empty string
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the table in bottom-up fashion
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    # '*' can match with any sequence: match zero characters (dp[i][j-1]) or match one more character (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    # '?' can match any single character, or the current characters match
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[len(s)][len(p)]

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
s1 = "aa"
p1 = "a"
print("Example 1:")
print("Input:", s1)
print("Output:", sol.isMatch(s1, p1))
print("=".center(50,"="))

# Example 2
s2 = "aa"
p2 = "*"
print("Example 2:")
print("Input:", s2)
print("Output:", sol.isMatch(s2, p2))
print("=".center(50,"="))

# Example 3
s3 = "cb"
p3 = "?a"
print("Example 2:")
print("Input:", s3)
print("Output:", sol.isMatch(s3, p3))
print("=".center(50,"="))