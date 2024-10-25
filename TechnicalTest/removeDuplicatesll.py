from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: If nums is empty, return 0 as there are no elements to process
        if not nums:
            return 0
        
        # Initialize two pointers: 'k' for the position to replace and 'count' for occurrences
        k = 1  # Start from index 1 as the first element can always stay
        count = 1  # First element has at least one occurrence
        
        # Iterate through nums starting from the second element
        for i in range(1, len(nums)):
            # If the current element is the same as the previous one, increment the count
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                # Reset count to 1 if we encounter a new element
                count = 1
            
            # If count is 1 or 2, place the element at the 'k' position and increment 'k'
            if count <= 2:
                nums[k] = nums[i]
                k += 1

        # Return the length of the modified array with each element appearing at most twice
        return k

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [1,1,1,2,2,3]
print("Example 1:", sol.removeDuplicates(nums1))
print("=".center(50,"="))

# Example 2
nums2 = [0,0,1,1,1,1,2,3,3]
print("Example 2:", sol.removeDuplicates(nums2))  
print("=".center(50,"="))