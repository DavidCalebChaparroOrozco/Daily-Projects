class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Create a set to store all the numbers for O(1) look-up time
        num_set = set(nums)
        
        # Initialize the variable to keep track of the longest sequence length
        longest_sequence = 0
        
        # Iterate through each number in the set
        for num in num_set:
            # Check if the current number is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_sequence = 1
                
                # Increment the current number and check if the next number exists in the set
                while current_num + 1 in num_set:
                    current_num += 1
                    current_sequence += 1
                
                # Update the longest sequence length if the current sequence is longer
                longest_sequence = max(longest_sequence, current_sequence)
        
        # Return the length of the longest consecutive sequence
        return longest_sequence
    
# Example usage:
sol = Solution()

# Example 1
print("=".center(50, "="))
nums1 = [100, 4, 200, 1, 3, 2]
print("Example 1:")
print("Input:", nums1)
print("Output:", sol.longestConsecutive(nums1))
print("=".center(50, "="))

# Example 2
print("Example 2:")
nums2 = [0,3,7,2,5,8,4,6,0,1]
print("Input:", nums2)
print("Output:", sol.longestConsecutive(nums2))
print("=".center(50, "="))

# Example 3
print("Example 3:")
nums3 = [1,2,0,1]
print("Input:", nums3)
print("Output:", sol.longestConsecutive(nums3))
print("=".center(50, "="))