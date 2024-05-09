# Given an integer array nums of length n and an integer target, 
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
class Solution(object):
    def threeSumClosest(self, nums, target):
        # Sort the array to facilitate search
        nums.sort()  
        
        # Initialize closest sum with infinity
        closest_sum = float('inf')  
        
        # Iterate over each number in the array, considering it as the possible first number of the triplet
        for i in range(len(nums) - 2):
            # Index of the second number
            left = i + 1  
            # Index of the third number
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # If current sum is equal to target, no need to continue searching
                if total == target:
                    return total
                
                # Update closest sum if current sum is closer to target
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                # Move indices based on the direction of current sum
                if total < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum


# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [-1,2,1,-4]
target1 = 1
print("Example 1:", sol.threeSumClosest(nums1, target1))
print("=".center(50,"="))

# Example 2
nums2 = [0 , 0, 0]
target2 = 1
print("Example 3:", sol.threeSumClosest(nums2, target2))  
print("=".center(50,"="))