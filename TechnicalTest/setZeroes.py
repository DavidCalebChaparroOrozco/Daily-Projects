class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # Get the dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        
        # Use two variables to track if the first row and first column should be set to zero
        first_row_has_zero = False
        first_col_has_zero = False
        
        # Check if the first row contains a zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        # Check if the first column contains a zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        
        # Use the first row and first column as markers
        # If matrix[i][j] is zero, mark matrix[i][0] and matrix[0][j] as zero
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set rows to zero based on the markers in the first column
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        # Set columns to zero based on the markers in the first row
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        # Finally, set the first row to zero if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Set the first column to zero if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print("Example 1:")
print("Input:", matrix1)
sol.setZeroes(matrix1)  
print("Output:", matrix1)  
print("=".center(50, "="))

# Example 2
matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print("Example 2:")
print("Input:", matrix2)
sol.setZeroes(matrix2)  
print("Output:", matrix2)  
print("=".center(50, "="))
