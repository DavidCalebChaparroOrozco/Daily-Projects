class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        This function searches for a target value in a matrix that has the following properties:
        - Each row is sorted in non-decreasing order.
        - The first integer of each row is greater than the last integer of the previous row.
        
        The goal is to implement a solution that has O(log(m * n)) time complexity, where m is the number
        of rows and n is the number of columns in the matrix.
        """
        if not matrix or not matrix[0]:
            # If the matrix is empty, return False
            return False  

        # Get the number of rows (m) and columns (n)
        m, n = len(matrix), len(matrix[0])

        # We can treat the matrix as a flat array and use binary search
        left, right = 0, m * n - 1  # Initial left and right boundaries for binary search

        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2  

            # Convert the mid index as if it's in a 1D array back to 2D matrix coordinates

            # Determine the row in the matrix
            row = mid // n  
            # Determine the column in the matrix
            col = mid % n   

            # Get the value at the mid index
            mid_value = matrix[row][col]  

            if mid_value == target:
                # Found the target
                return True  
            elif mid_value < target:
                # Narrow the search to the right half
                left = mid + 1  
            else:
                # Narrow the search to the left half
                right = mid - 1  

        # Target was not found
        return False  
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3
print("Example 1:")
print("Input:", matrix1)
print("Output:",sol.searchMatrix(matrix1, target1))
print("=".center(50, "="))

# Example 2
matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target2 = 13
print("Example 2:")
print("Input:", matrix2)
print("Output:", sol.searchMatrix(matrix2, target2))
print("=".center(50, "="))