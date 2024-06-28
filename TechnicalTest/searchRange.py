# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Finds the index of the first occurrence of the target in the sorted list nums.
        # If the target is not found, it returns -1.
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            first_pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first_pos = mid
                    right = mid - 1  # Keep searching on the left side
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_pos
        
        # Finds the index of the last occurrence of the target in the sorted list nums.
        # If the target is not found, it returns -1.
        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            last_pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last_pos = mid
                    left = mid + 1  # Keep searching on the right side
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_pos
        
        start = find_first(nums, target)
        end = find_last(nums, target)
        
        return [start, end]
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [5,7,7,8,8,10]
target1 = 8
print("Example 1:")
print("Input:", nums1)
print("Output:", sol.searchRange(nums1, target1))
print("=".center(50,"="))

# Example 2
nums2 = [5,7,7,8,8,10]
target2 = 6
print("Example 2:")
print("Input:", nums2)
print("Output:", sol.searchRange(nums2, target2))
print("=".center(50,"="))

# Example 3
num3 = []
target3 = 0
print("Example 2:")
print("Input:", num3)
print("Output:", sol.searchRange(num3, target3))
print("=".center(50,"="))