from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Initialize two pointers, left at the start and right at the end of the array
        left, right = 0, len(nums) - 1
        
        # Perform binary search to find a peak element
        while left < right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # If the middle element is greater than its right neighbor,
            # then there must be a peak in the left half (including mid)
            if nums[mid] > nums[mid + 1]:
                right = mid
            # Otherwise, the peak must be in the right half (excluding mid)
            else:
                left = mid + 1
                
        # When the loop ends, left and right converge to the peak element's index
        return left

# Create an instance of the Solution class to call the method
sol = Solution()

# Example 1: 
print("=".center(50,"="))
nums1 = [1, 2, 3, 1]
print("Example 1:")
print("Input:", nums1)
print("Output:", sol.findPeakElement(nums1)) 
print("=".center(50,"="))

# Example 2: 
nums2 = [1, 2, 1, 3, 5, 6, 4]
print("Example 2:")
print("Input:", nums2)
print("Output:", sol.findPeakElement(nums2))
print("=".center(50,"="))