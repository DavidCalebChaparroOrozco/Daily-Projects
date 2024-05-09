# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
# i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self, nums):
        # We sort the matrix to facilitate the search for triplets
        nums.sort()
        
        triplets = []
        
        # We iterate over each number in the array, considering it as the possible first number of the triplet
        for i in range(len(nums) - 2):
            # If the current number is equal to the previous one, we move to the next to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Second number index
            left = i + 1
            # Third number index
            right = len(nums) - 1
            
            # We look for the other two numbers to form the triplet
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    # We advance the indexes to avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return triplets


# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [-1,0,1,2,-1,-4]
print("Example 1:", sol.threeSum(nums1))
print("=".center(50,"="))

# Example 2
nums2 = [0 , 1, 1]
print("Example 2:", sol.threeSum(nums2))  
print("=".center(50,"="))

# Example 3
nums3 = [0 , 0, 0]
print("Example 3:", sol.threeSum(nums3))  
print("=".center(50,"="))