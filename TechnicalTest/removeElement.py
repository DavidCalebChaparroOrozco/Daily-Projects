# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are 
# not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, 
# you need to do the following things:
#  Change the array nums such that the first k elements of nums contain the elements which are 
#   not equal to val. The remaining elements of nums are not important as well as 
#   the size of nums.
#  Return k.


class Solution(object):
    def removeElement(self, nums, val):
        # Initialize the index for the next element that is not equal to val
        index = 0

        # Loop through each element in the array
        for i in range(len(nums)):
            # If the current element is not equal to val,
            # place it at the index position
            if nums[i] != val:
                nums[index] = nums[i]
                # Increment the index to prepare for the next element
                index += 1

        # The index now represents the number of elements in nums
        # that are not equal to val
        return index

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [3,2,2,3]
val1 = 3
print("Example 1:", sol.removeElement(nums1, val1))
print("=".center(50,"="))

# Example 2
nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
print("Example 2:", sol.removeElement(nums2, val2))
print("=".center(50,"="))