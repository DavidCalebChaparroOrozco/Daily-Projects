from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Sort the nums list to facilitate skipping duplicates
        nums.sort()
        # Initialize the result list to store all unique permutations
        result = []
        
        # Define a recursive helper function to generate permutations
        def backtrack(start: int):
            # Base case: if the start index is equal to the length of the nums list
            # it means we have a complete permutation
            if start == len(nums):
                # Append a copy of the current permutation to the result list
                result.append(nums[:])
                return
            
            # Use a set to track elements that have been used at the current position
            seen = set()
            
            # Iterate through the array to generate permutations
            for i in range(start, len(nums)):
                # Skip duplicate elements
                if nums[i] in seen:
                    continue
                
                # Add the element to the seen set
                seen.add(nums[i])
                
                # Swap the elements at indices start and i
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recursively call backtrack with the next index
                backtrack(start + 1)
                
                # Backtrack: revert the swap to restore the original order
                nums[start], nums[i] = nums[i], nums[start]
        
        # Start the backtracking process from the first index
        backtrack(0)
        
        # Return the list of all unique permutations
        return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [1,1,2]
print("Example 1:")
print("Input:", nums1)
print("Output:", sol.permuteUnique(nums1))
print("=".center(50,"="))

# Example 2
nums2 = [1,2,3]
print("Example 2:")
print("Input:", nums2)
print("Output:", sol.permuteUnique(nums2))
print("=".center(50,"="))