# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index 
# k (1 <= k < nums.length) such that the resulting array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Determine which part is sorted
            if nums[left] <= nums[mid]:
                # Left part is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right part is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [4,5,6,7,0,1,2]
target1 = 0
print("Example 1:")
print("Input:", nums1)
print("Output:", sol.search(nums1, target1))
print("=".center(50,"="))

# Example 2
nums2 = [4,5,6,7,0,1,2]
target2 = 3
print("Example 2:")
print("Input:", nums2)
print("Output:", sol.search(nums2, target2))
print("=".center(50,"="))

# Example 3
num3 = [1]
target3 = 0
print("Example 2:")
print("Input:", num3)
print("Output:", sol.search(num3, target3))
print("=".center(50,"="))