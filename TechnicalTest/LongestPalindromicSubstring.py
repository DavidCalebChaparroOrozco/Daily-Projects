# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Function to find the longest palindrome in a given string.
        if len(s) == 0:
            return ""
        
        start = 0
        end = 0
        
        # Iterate through the string.
        for i in range(len(s)):
            # Expand around the center to handle odd-length palindrome cases.
            len1 = self.expandAroundCenter(s, i, i)
            # Expand around the center to handle even-length palindrome cases.
            len2 = self.expandAroundCenter(s, i, i + 1)
            # Determine the maximum length between the two options.
            max_len = max(len1, len2)
            # Update the start and end indices of the longest palindrome found so far.
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        # Return the longest palindrome found in the string.
        return s[start:end+1]
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        # Function to expand around the center and find the length of the palindrome.
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the length of the palindrome found.
        return right - left - 1

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
s1 = "babad"
print("Example 1:")
print("Input:", s1)
print("Output:", sol.longestPalindrome(s1))
print("=".center(50,"="))

# Example 2
s2 = "cbbd"
print("Example 2:")
print("Input:", s2)
print("Output:", sol.longestPalindrome(s2))
print("=".center(50,"="))
