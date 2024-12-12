class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Get the lengths of the input strings
        len1, len2, len3 = len(s1), len(s2), len(s3)
        
        # If the lengths do not match, return False
        if len1 + len2 != len3:
            return False
        
        # Create a 2D DP table with (len1 + 1) x (len2 + 1)
        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        
        # Initialize the DP table
        dp[0][0] = True  # Both s1 and s2 are empty, so they can form an empty s3
        
        # Fill the first row (using only s1)
        for j in range(1, len2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
        # Fill the first column (using only s2)
        for i in range(1, len1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        
        # Fill in the rest of the DP table
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # Check if we can form s3 by taking a character from s1 or s2
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                        (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
        # The answer is whether we can form all of s3 using all of s1 and s2
        return dp[len1][len2]

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print("Example 1:")
print("Input:", s1, ",", s2, ",",  s3)
print("Output:", sol.isInterleave(s1,s2,s3))
print("=".center(50,"="))

# Example 2
s4 = "aabcc"
s5 = "dbbca"
s6 = "aadbbbaccc"
print("Example 2:")
print("Input:", s4, ",",  s5,  ",", s6)
print("Output:", sol.isInterleave(s4,s5,s6))
print("=".center(50,"="))

# Example 3
s7 = ""
s8 = ""
s9 = ""
print("Example 2:")
print("Input:", s7, s8, s9)
print("Output:", sol.isInterleave(s7, s8, s9))
print("=".center(50,"="))