class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words
        words = s.split()
        
        # Reverse the list of words
        reversed_words = words[::-1]
        
        # Join the reversed words with a single space
        return ' '.join(reversed_words)
    
# Example usage
sol = Solution()

# Example 1
print("=".center(50, "="))
s1 = "the sky is blue"
print("Example 1:")
print("Input:", s1)
print("Output:", sol.reverseWords(s1))
print("=".center(50, "="))

# Example 2
s2 = "  hello world  "
print("Example 2:")
print("Input:", s2)
print("Output:", sol.reverseWords(s2))
print("=".center(50, "="))

# Example 3
s3 = "a good   example"
print("Example 3:")
print("Input:", s3)
print("Output:", sol.reverseWords(s3))
print("=".center(50, "="))
