class Solution:
    # Merge two sorted arrays nums1 and nums2 into nums1 in-place.
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """    
        nums1: The first sorted array with a size of m + n, where the first m elements are valid.
        m: The number of valid elements in nums1.
        nums2: The second sorted array with n elements.
        n: The number of elements in nums2.
        """
        
        # Initialize pointers for the last elements of nums1 and nums2

        # Pointer for the last valid element in nums1
        indexNums1 = m - 1  
        # Pointer for the last element in nums2
        indexNums2 = n - 1  
        # Pointer for the last position in nums1
        mergedIndex = m + n - 1  

        # Iterate until all elements from nums2 are merged
        while indexNums2 >= 0:
            # If nums1 is exhausted or the current element in nums2 is larger
            if indexNums1 < 0 or nums1[indexNums1] <= nums2[indexNums2]:
                # Place the current element from nums2 into the correct position in nums1
                nums1[mergedIndex] = nums2[indexNums2]
                indexNums2 -= 1  # Move to the next element in nums2
            else:
                # Place the current element from nums1 into the correct position in nums1
                nums1[mergedIndex] = nums1[indexNums1]
                indexNums1 -= 1  # Move to the next element in nums1
            
            mergedIndex -= 1  # Move to the next position for merging

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
nums1 = [1, 2, 3, 0, 0, 0]
m1 = 3
n1 = 3
nums2 = [2, 5, 6]
print("Example 1:")
print("Input:", nums1)
sol.merge(nums1, m1, nums2, n1)
print("Output:", nums1)  
print("=".center(50, "="))

# Example 2
nums3 = [1]
m2 = 1
nums4 = []
n2 = 0
print("Example 2:")
print("Input:", nums3)
sol.merge(nums3, m2, nums4, n2)
print("Output:", nums3) 
print("=".center(50, "="))

# Example 3
nums5 = [0]
m3 = 0
nums6 = [1]
n3 = 1
print("Example 3:")
print("Input:", nums5)
sol.merge(nums5, m3, nums6, n3)
print("Output:", nums5)  
print("=".center(50, "="))