# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    # Finds the index where the target should be inserted in the sorted list nums.
    # If the target is already present in the list, it returns the index of the target.
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # If we exit the loop, left is the insertion point
        return left
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [1,3,5,6]
target1 = 5
print("Example 1:")
print("Input:", nums1)
print("Output:", sol.searchInsert(nums1, target1))
print("=".center(50,"="))

# Example 2
nums2 = [1,3,5,6]
target2 = 2
print("Example 2:")
print("Input:", nums2)
print("Output:", sol.searchInsert(nums2, target2))
print("=".center(50,"="))

# Example 3
num3 = [1,3,5,6]
target3 = 7
print("Example 2:")
print("Input:", num3)
print("Output:", sol.searchInsert(num3, target3))
print("=".center(50,"="))