class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip any trailing spaces to ensure we get the last word correctly
        s = s.rstrip()

        # Find the index of the last space in the trimmed string
        last_space_index = s.rfind(' ')

        # The length of the last word is the difference between the length of the string 
        # and the index of the last space. Adding 1 to the index because indices start from 0.
        return len(s) - last_space_index - 1

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
s1 = "Hello World"
print("Example 1:")
print("Input:", s1)
print("Output:", sol.lengthOfLastWord(s1))
print("=".center(50,"="))

# Example 2
s2 = "   fly me   to   the moon  "
print("Example 2:")
print("Input:", s2)
print("Output:", sol.lengthOfLastWord(s2))
print("=".center(50,"="))

# Example 3
s3 = "luffy is still joyboy"
print("Example 2:")
print("Input:", s3)
print("Output:", sol.lengthOfLastWord(s3))
print("=".center(50,"="))

