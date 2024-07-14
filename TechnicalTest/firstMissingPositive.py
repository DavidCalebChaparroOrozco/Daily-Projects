# Given an unsorted integer array nums. 
# Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Place each number in its right place if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap numbers to their correct positions
                correct_pos = nums[i] - 1
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        
        # After rearrangement, find the first place where the index doesn't match the value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positions are correct, the missing number is n + 1
        return n + 1

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
num1 = [1,2,0]
print("Example 1:")
print("Input:", num1)
print("Output:", sol.firstMissingPositive(num1))
print("=".center(50,"="))

# Example 2
num2 = [3,4,-1,1]
print("Example 2:")
print("Input:", num2)
print("Output:", sol.firstMissingPositive(num2, ))
print("=".center(50,"="))

# Example 3
num3 = [7,8,9,11,12]
print("Example 2:")
print("Input:", num3)
print("Output:", sol.firstMissingPositive(num3, ))
print("=".center(50,"="))