# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', 
#   assuming positivity is neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is 
#   encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
#   then round the integer to remain in the range. 
#   Specifically, integers less than -231 should be rounded to -231, 
#   and integers greater than 231 - 1 should be rounded to 231 - 1.

# Return the integer as the final result.

class Solution(object):
    def myAtoi(self, s):
        # Step 1: Ignore leading whitespaces
        s = s.lstrip()
        
        if not s:
            return 0
        
        # Step 2: Check the sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        # Step 3: Read digits and form the number
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
        
        # Apply the sign
        result *= sign
        
        # Step 4: Clamp to 32-bit signed integer range
        int_max = 2**31 - 1
        int_min = -2**31
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max
        
        return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = "42"
print("Example 1:", sol.myAtoi(nums1))
print("=".center(50,"="))

# Example 2
nums2 = " -042"
print("Example 2:", sol.myAtoi(nums2))  
print("=".center(50,"="))

# Example 3
nums3 = "1337c0d3"
print("Example 3:", sol.myAtoi(nums3))  
print("=".center(50,"="))

# Example 4
nums4 = "0-1"
print("Example 4:", sol.myAtoi(nums4))  
print("=".center(50,"="))

# Example 4
nums5 = "words and 987"
print("Example 4:", sol.myAtoi(nums4))  
print("=".center(50,"="))