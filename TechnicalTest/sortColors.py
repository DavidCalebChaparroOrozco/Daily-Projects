class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        This function sorts an array of integers representing colors in-place.
        The integers 0, 1, and 2 represent red, white, and blue respectively,
        and the array should be sorted in the order of red, white, and blue.
        
        The problem is solved using a variant of the Dutch National Flag algorithm
        to achieve O(n) time complexity and O(1) space complexity.
        """
        # Three pointers: low for red (0), high for blue (2), and current index i
        low, i, high = 0, 0, len(nums) - 1
        
        # Traverse the list and sort colors by swapping
        while i <= high:
            if nums[i] == 0:
                # Swap the current element (nums[i]) with nums[low] (red zone)
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
                i += 1
            elif nums[i] == 2:
                # Swap the current element (nums[i]) with nums[high] (blue zone)
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
            else:
                # If it's white (1), move the current pointer (i) forward
                i += 1

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
nums1 = [2,0,2,1,1,0]
print("Example 1:")
print("Input:", nums1)
sol.sortColors(nums1)
print("Output:", nums1) 
print("=".center(50, "="))

# Example 2
nums2 = [2,0,1]
print("Example 2:")
print("Input:", nums2)
sol.sortColors(nums2)
print("Output:", nums2)  
print("=".center(50, "="))