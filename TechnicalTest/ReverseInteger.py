# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range 
# [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        # If x is negative, we take its absolute value and then reverse it
        if x < 0:
            result = -int(str(-x)[::-1])
        else:
            result = int(str(x)[::-1])
        
        # Check if the result falls within the range of 32-bit integer
        if result < -2**31 or result > 2**31 - 1:
            return 0
        else:
            return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
x1 = 123
print("Example 1:")
print("Input:", x1)
print("Output:", sol.reverse(x1))
print("=".center(50,"="))

# Example 2
x2 = -123
print("Example 2:")
print("Input:", x2)
print("Output:", sol.reverse(x2))
print("=".center(50,"="))

# Example 3
x3 = 120
print("Example 3:")
print("Input:", x3)
print("Output:", sol.reverse(x3))
print("=".center(50,"="))
