# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store the numbers and their indices
        num_to_index = {}
        
        # Iterate over the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement that would sum to the target
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If it is, return the indices of the complement and the current number
                return [num_to_index[complement], index]
            
            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = index
        
        # If there is no solution, which shouldn't happen as per the problem constraints
        return []

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [2, 7, 11, 15]
target1 = 9
print("Example 1:", sol.twoSum(nums1, target1))
print("=".center(50,"="))

# Example 2
nums2 = [3 , 2, 4]
target2 = 6
print("Example 2:", sol.twoSum(nums2, target2))  
print("=".center(50,"="))

# Example 3
nums3 = [3,3]
target3 = 6
print("Example 3:", sol.twoSum(nums3, target3))  
print("=".center(50,"="))