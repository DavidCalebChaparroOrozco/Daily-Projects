class Solution:
    def singleNumber(self, nums: list[int]) -> int:
    # Initialize result to 0
        result = 0
        # Iterate through each number in the array
        for num in nums:
            # Perform XOR operation between result and current number
            # This cancels out duplicates and leaves the single number
            result ^= num
        
        # Return the single number
        return result
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
nums1 = [2, 2, 1]
print("Example 1:")
print("Input nums1:", nums1)
sol1 = sol.singleNumber(nums1)
print("Output:", sol1)
print("=".center(50, "="))

# Example 2
nums2 = [1, 2, 2]
print("Example 2:")
print("Input nums2:", nums2)
sol2 = sol.singleNumber(nums2)
print("Output:", sol2)
print("=".center(50, "="))

# Example 3
num3 = [1]
print("Example 3:")
print("Input nums3:", num3)
sol3 = sol.singleNumber(num3)
print("Output:", sol3)
print("=".center(50, "="))