from typing import List

class Solution:
    def findMinSortedArrayII(self, nums: List[int]) -> int:
        # Initialize two pointers: left at start and right at end of the array
        left, right = 0, len(nums) - 1
        
        # Perform binary search to find the minimum element
        while left < right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # If middle element is greater than rightmost element,
            # the minimum must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If middle element is less than rightmost element,
            # the minimum must be in the left half (including mid)
            elif nums[mid] < nums[right]:
                right = mid
            # When nums[mid] == nums[right], we can't determine which side
            # contains the minimum, so we reduce the search space from the right
            else:
                right -= 1
                
        # When the loop ends, left points to the minimum element
        return nums[left]

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
nums1 = [1, 3, 5]
print("Example 1:")
print("Input: ", nums1)
print("Output:", sol.findMinSortedArrayII(nums1))
print("=".center(50,"="))

# Example 2
nums2 = [2, 2, 2, 0, 1]
print("Example 2:")
print("Input: ", nums2)
print("Output: ",sol.findMinSortedArrayII(nums2))
print("=".center(50,"="))