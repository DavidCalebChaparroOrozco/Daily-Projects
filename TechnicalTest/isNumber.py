import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Regular expression to match a valid number
        pattern = re.compile(r'^[\+\-]?(\d+(\.\d*)?|\.\d+)([eE][\+\-]?\d+)?$')
        
        # Use the regular expression to match the input string
        # Return True if it matches, False otherwise
        return bool(pattern.match(s))
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
s1 = "0"
print("Example 1:")
print("Input:", s1)
print("Output:", sol.isNumber(s1))
print("=".center(50,"="))

# Example 2
s2 = "e"
print("Example 2:")
print("Input:", s2)
print("Output:", sol.isNumber(s2))
print("=".center(50,"="))


# Example 3
s3 = "."
print("Example 3:")
print("Input:", s3)
print("Output:", sol.isNumber(s3))
print("=".center(50,"="))