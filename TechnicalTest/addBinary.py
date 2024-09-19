class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize variables
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Traverse both strings from the end
        while i >= 0 or j >= 0 or carry:
            # Get the value of the current digit of 'a' or 'b', if within bounds
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum of digits plus carry
            total = digit_a + digit_b + carry
            carry = total // 2  # Calculate new carry (1 if total >= 2)
            result.append(str(total % 2))  # Append the current bit (total % 2)
            
            # Move to the previous digits
            i -= 1
            j -= 1
        
        # Join the result in reverse order (since we were adding from the end)
        return ''.join(reversed(result))

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
a1 = "11"
b1 = "1"
print("Example 1:")
print("Input:", a1)
print("Output:", sol.addBinary(a1, b1))
print("=".center(50,"="))

# Example 2
a2 = "1010"
b2 = "1011"
print("Example 2:")
print("Input:", a2)
print("Output:", sol.addBinary(a2, b2))
print("=".center(50,"="))