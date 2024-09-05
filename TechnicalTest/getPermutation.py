# Importing necessary libraries
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Initialize an empty result string to store the kth permutation
        result = ""
        
        # Create a list of numbers from 1 to n
        numbers = list(range(1, n + 1))
        
        # Adjust k to be zero-indexed (subtract 1 since k is 1-indexed)
        k -= 1

        # Iterate while there are numbers left to be placed in the result
        while n > 0:
            # Decrease n at each step
            n -= 1
            
            # Calculate the factorial of n (number of permutations per block)
            fact = math.factorial(n)
            
            # Determine the index of the current digit
            index = k // fact
            
            # Append the number at the index to the result
            result += str(numbers.pop(index))
            
            # Update k to reflect the position within the block
            k %= fact

        # Return the final kth permutation sequence
        return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
n1 = 3
k1 = 3
print("Example 1:")
print("Input:", n1)
print("Output:", sol.getPermutation(n1, k1))
print("=".center(50,"="))

# Example 2
n2 = 4
k2 = 9
print("Example 2:")
print("Input:", n2)
print("Output:", sol.getPermutation(n2, k2))
print("=".center(50,"="))

# Example 3
n3 = 3
k3 = 1
print("Example 2:")
print("Input:", n3)
print("Output:", sol.getPermutation(n3, k3))
print("=".center(50,"="))