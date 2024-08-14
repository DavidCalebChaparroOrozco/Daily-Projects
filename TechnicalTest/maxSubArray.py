class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize variables to store the maximum sum and the current sum


        # The maximum sum starts as the first element
        max_sum = nums[0]  
        # The current sum also starts as the first element
        current_sum = nums[0]  

        # Loop through the array starting from the second element
        for i in range(1, len(nums)):
            # Update the current sum by choosing the maximum between
            # the current element alone or the current element plus the previous sum.
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update the maximum sum if the current sum is greater
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum sum found
        return max_sum

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [-2,1,-3,4,-1,2,1,-5,4]
print("Example 1:")
print("Input:", nums1)
print("Output:", sol.maxSubArray(nums1))
print("=".center(50,"="))

# Example 2
nums2 = [1]
print("Example 2:")
print("Input:", nums2)
print("Output:", sol.maxSubArray(nums2))
print("=".center(50,"="))

# Example 3
nums3 = [5,4,-1,7,8]
print("Example 3:")
print("Input:", nums3)
print("Output:", sol.maxSubArray(nums3))
print("=".center(50,"="))
