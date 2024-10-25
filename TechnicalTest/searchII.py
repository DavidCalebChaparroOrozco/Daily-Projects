from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Edge case: if nums is empty, return False as no element can be found
        if not nums:
            return False
        
        # Initialize pointers for binary search
        left, right = 0, len(nums) - 1
        
        # Perform binary search with rotation handling
        while left <= right:
            mid = (left + right) // 2  # Find the middle index

            # Check if the target is at mid
            if nums[mid] == target:
                return True

            # To handle duplicates, move the pointers if the edges are equal to mid
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Left half is sorted
            elif nums[left] <= nums[mid]:
                # Check if the target lies in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Narrow search to the left
                else:
                    left = mid + 1  # Narrow search to the right
            # Right half is sorted
            else:
                # Check if the target lies in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Narrow search to the right
                else:
                    right = mid - 1  # Narrow search to the left
        
        # If the loop ends, the target is not in the array
        return False

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [2,5,6,0,0,1,2]
target1 = 0
print("Example 1:", sol.search(nums1, target1))
print("=".center(50,"="))

# Example 2
nums2 = [2,5,6,0,0,1,2]
target2 = 3
print("Example 2:", sol.search(nums2, target2))  
print("=".center(50,"="))