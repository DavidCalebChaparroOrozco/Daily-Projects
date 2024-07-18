# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # If the height list is empty, no water can be trapped
        if not height:
            return 0

        # Initialize two pointers for left and right boundaries
        left, right = 0, len(height) - 1
        # Initialize the maximum heights seen so far from the left and right
        left_max, right_max = height[left], height[right]
        # Variable to store the total amount of water trapped
        water_trapped = 0

        # Iterate until the left pointer crosses the right pointer
        while left < right:
            if left_max < right_max:
                # Move the left pointer to the right
                left += 1
                # Update the maximum height seen from the left
                left_max = max(left_max, height[left])
                # Calculate and add the trapped water at the current position
                water_trapped += left_max - height[left]
            else:
                # Move the right pointer to the left
                right -= 1
                # Update the maximum height seen from the right
                right_max = max(right_max, height[right])
                # Calculate and add the trapped water at the current position
                water_trapped += right_max - height[right]

        # Return the total amount of water trapped
        return water_trapped

    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
print("Example 1:")
print("Input:", height1)
print("Output:", sol.trap(height1))
print("=".center(50,"="))

# Example 2
height2 = [4,2,0,3,2,5]
print("Example 2:")
print("Input:", height2)
print("Output:", sol.trap(height2))
print("=".center(50,"="))