# Given an input string s and a pattern p, implement regular expression matching with support 
# for '.' and '*' where:
#     '.' Matches any single character.​​​​
#     '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

class Solution(object):
    def isMatch(self, s, p):
        # Create a 2D DP table to store the results of subproblems
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: empty pattern matches empty string
        dp[0][0] = True
        
        # Fill the first row of the DP table
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        
        # Return the result which is at the bottom-right corner of the DP table
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
p2 = "a*"
print("Example 2:")
print("Input:", s2)
print("Output:", sol.isMatch(s2, p2))
print("=".center(50,"="))

# Example 3
s3 = "ab"
p3 = ".*"
print("Example 3:")
print("Input:", s3)
print("Output:", sol.isMatch(s3,p3))
print("=".center(50,"="))
