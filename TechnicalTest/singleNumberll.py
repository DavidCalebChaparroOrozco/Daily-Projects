class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # Initialize result to 0
        result = 0
        # Iterate over each bit position (0 to 31)
        for i in range(32):
            # Count the number of set bits at the current position
            bit_count = 0
            for num in nums:
                # Right-shift the number by 'i' and check if the least significant bit is set
                if (num >> i) & 1:
                    bit_count += 1
            
            # If the count is not divisible by 3, set the bit in the result
            if bit_count % 3 != 0:
                # For negative numbers (handling two's complement)
                if i == 31:
                    # Adjust for the sign bit in 32-bit integers
                    result -= (1 << i)  
                else:
                    # Set the bit in the result
                    result |= (1 << i)  
        
        return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
nums1 = [2, 2, 3, 2]
print("Example 1:")
print("Input nums1:", nums1)
sol1 = sol.singleNumber(nums1)
print("Output:", sol1)
print("=".center(50, "="))

# Example 2
nums2 = [0, 1, 0, 1, 0, 1, 99]
print("Example 2:")
print("Input nums2:", nums2)
sol2 = sol.singleNumber(nums2)
print("Output:", sol2)
print("=".center(50, "="))