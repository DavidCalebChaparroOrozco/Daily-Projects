from typing import List

class Solution:
    # Generate an n-bit Gray code sequence.
    def grayCode(self, n: int) -> List[int]:
        """
        n: The number of bits in the Gray code.

        Returns:
        : A list containing the n-bit Gray code sequence.
        """
        
        # Initialize the list to hold the Gray code sequence
        gray_code_sequence = []
        
        # The number of Gray codes for n bits is 2^n
        total_codes = 1 << n  # This is equivalent to 2 ** n
        
        # Generate the Gray code sequence
        for i in range(total_codes):
            # The formula to convert i to its corresponding Gray code is i ^ (i >> 1)
            gray_code = i ^ (i >> 1)
            # Append the generated Gray code to the list
            gray_code_sequence.append(gray_code)  
        
        return gray_code_sequence

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
n1 = 2
print("Example 1:")
print("Input:", n1)
print("Output:", sol.grayCode(n1))
print("=".center(50,"="))

# Example 2
n2 = 1
print("Example 2:")
print("Input:", n2)
print("Output:", sol.grayCode(n2))
print("=".center(50,"="))