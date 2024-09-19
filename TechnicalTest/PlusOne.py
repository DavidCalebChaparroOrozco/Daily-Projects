class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):
            # If the digit is less than 9, we can simply add 1 and return the list
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, we set it to 0 and continue to the next digit
            digits[i] = 0
        
        # If all digits were 9, the result would be a new list starting with 1 followed by zeros
        return [1] + digits

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
digits1 = [1,2,3]
print("Example 1:")
print("Input:", digits1)
print("Output:", sol.plusOne(digits1))
print("=".center(50,"="))

# Example 2
digits2 = [4,3,2,1]
print("Example 2:")
print("Input:", digits2)
print("Output:", sol.plusOne(digits2))
print("=".center(50,"="))

# Example 3
digits3 = [9]
print("Example 2:")
print("Input:", digits3)
print("Output:", sol.plusOne(digits3))
print("=".center(50,"="))