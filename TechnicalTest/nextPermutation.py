# Implement the next permutation, which rearranges numbers into the lexicographically next greater 
# permutation of numbers. If such an arrangement is not possible, it must rearrange it as the 
# lowest possible order (i.e., sorted in ascending order). 
# The replacement must be in place and use only constant extra memory.

# Importing necessary libraries
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Step 1: Find the first decreasing element from the end
        k = len(nums) - 2
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1
        
        # if the array is not entirely in descending order
        if k >= 0:  
            # Step 2: Find the element to swap with
            l = len(nums) - 1
            while l >= 0 and nums[l] <= nums[k]:
                l -= 1
            
            # Step 3: Swap elements
            nums[k], nums[l] = nums[l], nums[k]
        
        # Step 4: Reverse the subarray starting from k+1
        self.reverse(nums, k + 1, len(nums) - 1)
    
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

# Create an instance of the Solution class
sol = Solution()

# Example 1
nums = [1, 2, 3]
sol.nextPermutation(nums)
print("Example 1:",nums)
print("=".center(50,"="))

# Example 2
nums = [3, 2, 1]
sol.nextPermutation(nums)
print("Example 2:",nums)
print("=".center(50,"="))

# Example 3
nums = [1, 1, 5]
sol.nextPermutation(nums)
print("Example 3:",nums)
print("=".center(50,"="))
