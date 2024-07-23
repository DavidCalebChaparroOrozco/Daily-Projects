# You are given a 0-indexed array of integers nums of length n. 
# You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. 
# In other words, if you are at nums[i], you can jump to any nums[i + j] where:

#     0 <= j <= nums[i] and
#     i + j < n

# Return the minimum number of jumps to reach nums[n - 1]. 
# The test cases are generated such that you can reach nums[n - 1].

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            # If there is only one element, no jump is needed
            return 0  

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break

        return jumps

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [2, 3, 1, 1, 4]
print("Example 1:")
print("Input:", nums1)
print("Output:", sol.jump(nums1))
print("=".center(50,"="))

# Example 2
num2 = [2, 3, 0, 1, 4]
print("Example 2:")
print("Input:", num2)
print("Output:", sol.jump(num2))
print("=".center(50,"="))