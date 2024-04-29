# Given a string s, find the length of the longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Dictionary to store the index of each character's last occurrence
        char_index = {}
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            # If the character is already in the dictionary and its index is greater than or equal to start
            if s[end] in char_index and char_index[s[end]] >= start:
                # Move the start of the window to the right of the previous occurrence of the character
                start = char_index[s[end]] + 1
            # Update the index of the character
            char_index[s[end]] = end
            # Update the maximum length
            max_length = max(max_length, end - start + 1)
        
        return max_length
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
s1 = "abcabcbb"
print("Example 1:", sol.lengthOfLongestSubstring(s1))
print("=".center(50,"="))

# Example 2
s2 = "bbbbb"
print("Example 2:", sol.lengthOfLongestSubstring(s2))  
print("=".center(50,"="))

# Example 3
s3 = "pwwkew"
print("Example 3:", sol.lengthOfLongestSubstring(s3))  
print("=".center(50,"="))