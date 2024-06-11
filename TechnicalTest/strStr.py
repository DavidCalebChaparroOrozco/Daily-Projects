# Given two strings needle and haystack, return the index of the first occurrence of needle
# in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is an empty string, return 0 as per the problem's requirements
        if not needle:
            return 0
        # Use the find method to get the index of the first occurrence
        return haystack.find(needle)
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
haystack1 = "sadbutsad"
needle1 = "sad"
print("Example 1:", sol.strStr(haystack1, needle1))
print("=".center(50,"="))

# Example 2
haystack2 = "leetcode"
needle2 = "leeto"
print("Example 2:", sol.strStr(haystack2, needle2))  
print("=".center(50,"="))