from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # First, transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Second, reverse each row
        for i in range(n):
            matrix[i].reverse()

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print("Example 1:")
print("Input:", matrix1)
sol.rotate(matrix1)
print("Output:", matrix1)
print("=".center(50,"="))

# Example 2
matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print("Example 2:")
print("Input:", matrix2)
sol.rotate(matrix2)
print("Output:", matrix2)
print("=".center(50,"="))