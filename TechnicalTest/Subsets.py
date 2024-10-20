from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # This function will return all possible subsets of the input list 'nums'
        
        # Initialize the result list with an empty subset
        result = [[]]
        
        # Loop through each number in the input list
        for num in nums:
            # For each number, add it to all existing subsets to create new subsets
            # and extend the result list with these new subsets
            result += [curr + [num] for curr in result]
        
        # Return the complete list of subsets
        return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
nums1 = [1, 2, 3]
print("Example 1:")
print("Input:", nums1)
print("Output:",sol.subsets(nums1))
print("=".center(50, "="))

# Example 2
nums2 = [0]
print("Example 2:")
print("Input:", nums2) 
print("Output:", sol.subsets(nums2))
print("=".center(50, "="))