from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        
        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        # Each bucket stores [min, max]
        buckets = [[None, None] for _ in range(bucket_count)]  
        
        # Distribute numbers into buckets
        for num in nums:
            bucket_index = (num - min_val) // bucket_size
            bucket = buckets[bucket_index]
            if bucket[0] is None:
                bucket[0] = bucket[1] = num
            else:
                bucket[0] = min(bucket[0], num)
                bucket[1] = max(bucket[1], num)
        
        # Calculate the maximum gap between buckets
        max_gap = 0
        previous_max = buckets[0][1]
        for i in range(1, bucket_count):
            if buckets[i][0] is not None:
                current_min = buckets[i][0]
                max_gap = max(max_gap, current_min - previous_max)
                previous_max = buckets[i][1]
        
        return max_gap
    

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
nums1 = [3, 6, 9, 1]
print("Example 1:")
print("Input:", nums1)
print("Output:", sol.maximumGap(nums1))

# Example 2
print("=".center(50, "="))
nums2 = [10]
print("Example 2:")
print("Input:", nums2)
print("Output:", sol.maximumGap(nums2))
print("=".center(50, "="))