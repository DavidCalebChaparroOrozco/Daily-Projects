# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array to optimize the binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        # Initialize binary search boundaries
        start, end = 0, m
        
        while start <= end:
            partition_nums1 = (start + end) // 2
            partition_nums2 = (m + n + 1) // 2 - partition_nums1
            
            max_left_nums1 = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            min_right_nums1 = float('inf') if partition_nums1 == m else nums1[partition_nums1]
            
            max_left_nums2 = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            min_right_nums2 = float('inf') if partition_nums2 == n else nums2[partition_nums2]
            
            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                # Found the correct partition
                if (m + n) % 2 == 0:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2.0
                else:
                    return float(max(max_left_nums1, max_left_nums2))
            elif max_left_nums1 > min_right_nums2:
                # Move left in nums1
                end = partition_nums1 - 1
            else:
                # Move right in nums1
                start = partition_nums1 + 1

# Create an instance of the Solution class
sol = Solution()

# Example 1
nums1 = [1,3]
nums2 = [2]

# Print the median of nums1 and nums2
print("Example 1: ",sol.findMedianSortedArrays(nums1, nums2))
# Print a separator line
print("=".center(50,"="))

# Example 2
nums3 = [1,2]
nums4 = [3,4]

# Print the median of nums3 and nums4
print("Example 2: ",sol.findMedianSortedArrays(nums3, nums4))
# Print a separator line
print("=".center(50,"="))
