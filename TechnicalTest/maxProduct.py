class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Initialize variables to store the current max, current min, and the result
        current_max = current_min = result = nums[0]
        
        for num in nums[1:]:
            # Temporary variable to store current_max because it might change before calculating current_min
            temp_max = current_max
            # The new current_max can be the product of current_max and num, current_min and num, or just num (starting a new subarray)
            current_max = max(num, temp_max * num, current_min * num)
            # Similarly, the new current_min can be the product of current_min and num, previous current_max and num, or just num
            current_min = min(num, temp_max * num, current_min * num)
            
            # Update the overall result
            result = max(result, current_max)
        
        return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [2,3,-2,4]
print("Example 1:")
print("Input nums1:", nums1)
print("Output:", sol.maxProduct(nums1))

# Example 2
print("=".center(50,"="))
nums2 = [-2,0,-1]
print("Example 2:")
print("Input prices:", nums2)
print("Output:", sol.maxProduct(nums2))
print("=".center(50,"="))