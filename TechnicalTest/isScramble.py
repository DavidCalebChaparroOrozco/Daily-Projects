class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # Memoization dictionary
        memo = {}
        
        def helper(s1: str, s2: str) -> bool:
            # Check if the strings are already equal
            if s1 == s2:
                return True
            
            # Check if sorted characters match
            if sorted(s1) != sorted(s2):
                return False
            
            # Use memoization to save results for (s1, s2)
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            
            n = len(s1)
            # Try all possible split points
            for i in range(1, n):  # Splitting at index i
                # Check both possible scenarios
                if (helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:])) or \
                   (helper(s1[:i], s2[-i:]) and helper(s1[i:], s2[:-i])):
                    memo[(s1, s2)] = True
                    return True
            
            # If no valid scramble found, store result as False
            memo[(s1, s2)] = False
            return False
        
        return helper(s1, s2)
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
s1 = "great"
s2 = "rgeat"
print("Example 1:")
print("Input:", s1, "-", s2)
output1 = sol.isScramble(s1, s2)
print("Output:", output1)
print("=".center(50, "="))

# Example 2
s3 = "abcde"
s4 = "caebd"
print("Example 2:")
print("Input:", s3, "-", s4)
output2 = sol.isScramble(s3, s4)
print("Output:", output2)
print("=".center(50, "="))

# Example 3
s5 = "a"
s6 = "a"
print("Example 3:")
print("Input:", s5, "-", s6)
output3 = sol.isScramble(s5, s6)
print("Output:", output3)
print("=".center(50, "="))
