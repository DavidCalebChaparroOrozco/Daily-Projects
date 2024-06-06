# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
# such that each unique element appears only once. The relative order of the elements should 
# be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the 
# following things:
#  Change the array nums such that the first k elements of nums contain the unique elements in the order they 
#   were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
#  Return k.

class Solution(object):
    def removeDuplicates(self, nums):
        # If the array is empty, return 0 since there are no elements
        if not nums:
            return 0

        # Initialize the index for the next unique element
        unique_index = 1

        # Loop through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous element,
            # it means it's a unique element
            if nums[i] != nums[i - 1]:
                # Place the unique element at the unique_index position
                nums[unique_index] = nums[i]
                # Increment the unique_index to prepare for the next unique element
                unique_index += 1

        # The unique_index now represents the number of unique elements
        return unique_index

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [1,1,2]
print("Example 1:", sol.removeDuplicates(nums1))
print("=".center(50,"="))

# Example 2
nums2 = [0,0,1,1,1,2,2,3,3,4]
print("Example 2:", sol.removeDuplicates(nums2))  
print("=".center(50,"="))