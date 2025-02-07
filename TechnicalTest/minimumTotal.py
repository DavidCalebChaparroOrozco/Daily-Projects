from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # If the triangle is empty, return 0
        if not triangle:
            return 0
        
        # Initialize n as the number of rows in the triangle
        n = len(triangle)
        
        # Start from the second last row and move upwards
        for i in range(n - 2, -1, -1):
            # For each element in the current row
            for j in range(len(triangle[i])):
                # Update its value with the minimum path sum it can achieve by moving down or diagonally
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        
        # The minimum path sum will be stored at the top of the updated triangle
        return triangle[0][0]

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
print("Example 1:")
print("Input triangle:", triangle1)
print("Output:", sol.minimumTotal(triangle1))

# Example 2
print("=".center(50,"="))
triangle2 = [[-10]]
print("Example 2:")
print("Input triangle:", triangle2)
print("Output:", sol.minimumTotal(triangle2))
print("=".center(50,"="))