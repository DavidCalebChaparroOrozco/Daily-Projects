from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize an n x n matrix filled with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Define the starting points for the spiral traversal
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        
        # Start filling the matrix with numbers from 1 to n^2
        num = 1
        max_num = n * n
        
        # Continue filling the matrix while the number is less than or equal to n^2
        while num <= max_num:
            # Fill the top row from left to right
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1  # Move the top boundary downwards
            
            # Fill the right column from top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1  # Move the right boundary to the left
            
            # Fill the bottom row from right to left
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1  # Move the bottom boundary upwards
            
            # Fill the left column from bottom to top
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1  # Move the left boundary to the right
        
        # Return the filled spiral matrix
        return matrix

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
n1 = 3
print("Example 1:")
print("Input:", n1)
print("Output:", sol.generateMatrix(n1))
print("=".center(50,"="))

# Example 2
n2 = 1
print("Example 2:")
print("Input:", n2)
print("Output:", sol.generateMatrix(n2))
print("=".center(50,"="))