# Container With Most Water(maxArea)
# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are 
# (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains 
# the most water.
# Return the maximum amount of water a container can store.

class Solution(object):
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the current area
            current_area = min(height[left], height[right]) * (right - left)
            # Update the maximum area found so far
            max_area = max(max_area, current_area)
            
            # Move the pointer that is at the lowest height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
height1 = [1,8,6,2,5,4,8,3,7]
print("Example 1:")
print("Input:", height1)
print("Output:", sol.maxArea(height1))
print("=".center(50,"="))

# Example 2
height2 = [1,1]
print("Example 2:")
print("Input:", height2)
print("Output:", sol.maxArea(height2))
print("=".center(50,"="))
