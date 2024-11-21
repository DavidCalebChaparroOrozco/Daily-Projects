class Solution:
    def numDecodings(self, s: str) -> int:
        # If the string is empty, there is one way to decode it (by decoding nothing)
        if not s:
            return 0
        
        # Length of the input string
        n = len(s)
        
        # dp array to store the number of ways to decode up to each index
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # An empty string has one way to be decoded
        dp[1] = 1 if s[0] != '0' else 0  # A single character can only be decoded if it's not '0'
        
        for i in range(2, n + 1):
            # Check the last single digit
            one_digit = int(s[i-1:i])  # Get the last one digit
            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]
            
            # Check the last two digits
            two_digits = int(s[i-2:i])  # Get the last two digits
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
s1 = "123"
print("Example 1:")
print("Input:", s1)
print("Output:", sol.numDecodings(s1))
print("=".center(50,"="))

# Example 2
s2 = "226"
print("Example 2:")
print("Input:", s2)
print("Output:", sol.numDecodings(s2))
print("=".center(50,"="))

# Example 3
s3 = "06"
print("Example 2:")
print("Input:", s3)
print("Output:", sol.numDecodings(s3))
print("=".center(50,"="))