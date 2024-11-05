from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Check if the matrix is empty
        if not matrix or not matrix[0]:
            return 0
        
        # Initialize variables for dimensions and maximum area
        rows, cols = len(matrix), len(matrix[0])
        max_area = 0
        heights = [0] * cols  # Array to store the heights of histogram bars

        # Iterate through each row of the matrix
        for row in matrix:
            # Update the heights array based on the current row
            for col in range(cols):
                # Increase the height if there's a '1', otherwise reset to 0
                heights[col] = heights[col] + 1 if row[col] == '1' else 0
            
            # Calculate the largest rectangle area for the current row's histogram
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        # This helper function calculates the largest rectangle in a histogram
        stack = []
        max_area = 0
        heights.append(0)  # Append a zero to ensure all bars are processed

        for i in range(len(heights)):
            # Process bars in a descending order by popping from the stack
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Height of the bar at the stack top
                # Calculate width based on stack
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)  # Update maximum area
            # Push current index to stack
            stack.append(i)
        
        heights.pop()  # Restore the original heights array by removing the added 0
        return max_area

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
matrix1 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print("Example 1:")
print("Input matrix1:", matrix1 )
print("Output:", sol.maximalRectangle(matrix1))
print("=".center(50,"="))

# Example 2
matrix2 = [["0"]]
print("Example 2:")
print("Input matrix2:", matrix2)
print("Output:", sol.maximalRectangle(matrix2))
print("=".center(50,"="))

# Example 3
matrix3 = [["1"]]
print("Example 2:")
print("Input matrix3:", matrix3)
print("Output:", sol.maximalRectangle(matrix3))
print("=".center(50,"="))