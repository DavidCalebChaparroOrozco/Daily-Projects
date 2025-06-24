class Solution:
    # This function finds the minimum element in a rotated sorted array.
    def findMin(self, nums: list[int]) -> int:
        # Check if the list is empty
        left, right = 0, len(nums) - 1
        
        # If the list is not rotated, return the first element
        while left < right:
            # Calculate the middle index
            mid = (left + right) // 2
            # If the middle element is greater than the rightmost element,
            # it means the minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        # When left equals right, we have found the minimum element
        return nums[left]

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
nums1 = [3, 4, 5, 1, 2]
print("Example 1:")
print("Input nums1:", nums1)
print("Output:", sol.findMin(nums1))

# Example 2
print("=".center(50, "="))
nums2 = [4, 5, 6, 7, 0, 1, 2]
print("Example 2:")
print("Input nums2:", nums2)
print("Output:", sol.findMin(nums2))

# Example 3
print("=".center(50, "="))
nums3 = [11, 13, 15, 17]
print("Example 3:")
print("Input nums3:", nums3)
print("Output:", sol.findMin(nums3))
print("=".center(50, "="))