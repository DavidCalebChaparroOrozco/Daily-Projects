from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Initialize a stack to keep track of the indices of the histogram bars.
        stack = []
        max_area = 0  # Variable to store the maximum area found
        
        # Append a zero height to ensure all bars are processed in the end.
        heights.append(0)
        
        # Traverse each bar in the histogram.
        for i in range(len(heights)):
            # While the current bar is shorter than the last bar in the stack
            # we can calculate the area with the height of the bar at the stack's top.
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Height of the bar we are processing
                # If stack is empty, width is the full range from start to the current index i.
                # Otherwise, width is between the current index and the new top of stack.
                w = i if not stack else i - stack[-1] - 1
                # Calculate the area and update max_area if this area is larger.
                max_area = max(max_area, h * w)
            # Push the current bar index to the stack.
            stack.append(i)
        
        # Remove the appended zero height to restore the original heights list.
        heights.pop()
        
        return max_area

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
heights1 = [2,1,5,6,2,3]
print("Example 1:")
print("Input heights1:", heights1 )
print("Output:", sol.largestRectangleArea(heights1))
print("=".center(50,"="))

# Example 2
heights2 = [2,4]
print("Example 2:")
print("Input heights2:", heights2)
print("Output:", sol.largestRectangleArea(heights2))
print("=".center(50,"="))