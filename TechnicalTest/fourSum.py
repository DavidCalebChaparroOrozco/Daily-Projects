# Given an array nums of n integers, return an array of all the unique quadruplets 
# [nums[a], nums[b], nums[c], nums[d]] such that:
#     0 <= a, b, c, d < n
#     a, b, c, and d are distinct.
#     nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()  # Sort the array to facilitate binary search
        n = len(nums)
        result = []

        # Iterate over the first two elements
        for i in range(n - 3):
            # Avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Reduce the problem to three sum search
            for j in range(i + 1, n - 2):
                # Avoid duplicates
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Define two pointers to find the other two sums
                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Avoid duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = [1,0,-1,0,-2,2]
target1 = 0
print("Example 1:")
print("Input:", nums1)
print("Output:", sol.fourSum(nums1,target1))
print("=".center(50,"="))

# Example 2
nums2 = [2,2,2,2,2]
target2 = 8
print("Example 2:")
print("Input:", nums2)
print("Output:", sol.fourSum(nums2,target2))
print("=".center(50,"="))