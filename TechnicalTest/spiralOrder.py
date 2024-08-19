from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        if not matrix or not matrix[0]:
            return result
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # Traverse from right to left along the bottom row
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                # Traverse from bottom to top along the left column
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print("Example 1:")
print("Input:", matrix1)
print("Output:", sol.spiralOrder(matrix1))
print("=".center(50,"="))

# Example 2
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print("Example 2:")
print("Input:", matrix2)
print("Output:", sol.spiralOrder(matrix2))
print("=".center(50,"="))