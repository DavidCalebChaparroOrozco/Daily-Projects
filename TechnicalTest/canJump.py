from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # max_reachable will keep track of the farthest index we can reach
        max_reachable = 0
        # n is the length of the nums array
        n = len(nums)
        
        # Loop through each index in the array
        for i in range(n):
            # If the current index is greater than the maximum reachable index,
            # it means we can't reach this point, so return False
            if i > max_reachable:
                return False
            
            # Update max_reachable to the farthest index we can reach from the current position
            max_reachable = max(max_reachable, i + nums[i])
            
            # If at any point max_reachable is beyond or at the last index,
            # return True because we can reach the last index
            if max_reachable >= n - 1:
                return True
        
        # After the loop, return whether we can reach or pass the last index
        return max_reachable >= n - 1

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [2,3,1,1,4]
print("Example 1:")
print("Input:", nums1)
print("Output:", sol.canJump(nums1))
print("=".center(50,"="))

# Example 2
nums2 = [3,2,1,0,4]
print("Example 2:")
print("Input:", nums2)
print("Output:", sol.canJump(nums2))
print("=".center(50,"="))