# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

#  countAndSay(1) = "1"
#  countAndSay(n) is the run-length encoding of countAndSay(n - 1).

# Run-length encoding (RLE) is a string compression method that works by replacing consecutive
# identical characters (repeated 2 or more times) with the concatenation of the character and 
# the number marking the count of the characters (length of the run). For example, to compress 
# the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with 
# "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

# Given a positive integer n, return the nth element of the count-and-say sequence.

class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        
        # Recursive call to get the (n-1)th sequence
        prev_sequence = self.countAndSay(n - 1)
        
        # Initialize the result string and a counter
        result = ""
        count = 1
        
        # Loop through the previous sequence
        for i in range(1, len(prev_sequence)):
            # If the current character is the same as the previous one, increment the count
            if prev_sequence[i] == prev_sequence[i - 1]:
                count += 1
            else:
                # Otherwise, append the count and the character to the result
                result += str(count) + prev_sequence[i - 1]
                # Reset the count to 1
                count = 1
        
        # Append the count and character for the last group of characters
        result += str(count) + prev_sequence[-1]
        
        return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nums1 = 4
print("Example 1:")
print("Input:", nums1)
print("Output:", sol.countAndSay(nums1))
print("=".center(50,"="))

# Example 2
nums2 = 1
print("Example 2:")
print("Input:", nums2)
print("Output:", sol.countAndSay(nums2))
print("=".center(50,"="))