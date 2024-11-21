from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to handle duplicates easily
        nums.sort()
        
        # This will hold all the unique subsets
        result = []
        
        # Helper function to generate subsets
        def backtrack(start: int, path: List[int]):
            # Append the current subset (path) to the result
            result.append(path.copy())
            
            for i in range(start, len(nums)):
                # If the current number is the same as the previous one, skip it to avoid duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Include nums[i] in the current subset
                path.append(nums[i])
                
                # Move on to the next element
                backtrack(i + 1, path)
                
                # Backtrack: remove the last element before moving to the next iteration
                path.pop()
        
        # Start backtracking from index 0 with an empty path
        backtrack(0, [])
        
        return result
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [1,2,2]
print("Example 1:")
print("Input:", nums1)
print("Output:", sol.subsetsWithDup(nums1))
print("=".center(50,"="))

# Example 2
nums2 = [0]
print("Example 2:")
print("Input:", nums2)
print("Output:", sol.subsetsWithDup(nums2))
print("=".center(50,"="))