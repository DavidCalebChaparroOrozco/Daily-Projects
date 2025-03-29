class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # Create a DP table to store if s[i..j] is a palindrome
        is_palindrome = [[False for _ in range(n)] for _ in range(n)]
        
        # Every single character is a palindrome
        for i in range(n):
            is_palindrome[i][i] = True
        
        # Check for substrings of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                is_palindrome[i][i+1] = True
        
        # Check for substrings longer than 2
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and is_palindrome[i+1][j-1]:
                    is_palindrome[i][j] = True
        
        # Now, compute the minimum cuts
        min_cuts = [0] * n
        
        for i in range(n):
            # If s[0..i] is already a palindrome, no cut needed
            if is_palindrome[0][i]:
                min_cuts[i] = 0
            else:
                # Initialize with maximum possible cuts
                min_cuts[i] = float('inf')
                # Check for all possible partitions
                for j in range(i):
                    if is_palindrome[j+1][i] and min_cuts[j] + 1 < min_cuts[i]:
                        min_cuts[i] = min_cuts[j] + 1
        
        return min_cuts[n-1]
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
s1 = "aab"
print("Example 1:")
print("Input s1:", s1)
sol1 = sol.minCut(s1)
print("Output:", sol1)
print("=".center(50, "="))

# Example 2
s2 = "a"
print("Example 2:")
print("Input s2:", s2)
sol2 = sol.minCut(s2)
print("Output:", sol2)
print("=".center(50, "="))

# Example 3
s3 = "ab"
print("Example 3:")
print("Input s3:", s3)
sol3 = sol.minCut(s3)
print("Output:", sol3)
print("=".center(50, "="))
