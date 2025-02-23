class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: one at the start and one at the end of the string
        left, right = 0, len(s) - 1
        
        # Loop until the two pointers meet
        while left < right:
            # Move the left pointer to the right if the current character is not alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move the right pointer to the left if the current character is not alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare the characters at the left and right pointers (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False  # Not a palindrome
            
            # Move the pointers towards the center
            left += 1
            right -= 1
        
        # If the loop completes, the string is a palindrome
        return True

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
s1 = "A man, a plan, a canal: Panama"
print("Example 1:")
print("Input string:", s1)
print("Output:", sol.isPalindrome(s1))

# Example 2
print("=".center(50, "="))
s2 = "race a car"
print("Example 2:")
print("Input string:", s2)
print("Output:", sol.isPalindrome(s2))

# Example 3
print("=".center(50, "="))
s3 = " "
print("Example 3:")
print("Input string:", s3)
print("Output:", sol.isPalindrome(s3))
print("=".center(50, "="))