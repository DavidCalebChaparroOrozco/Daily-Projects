from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        # Empty string can be segmented
        dp[0] = True  
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
s1 = "leetcode"
wordDict1 = ["leet", "code"]
print("Example 1:")
print("Input s1:", s1)
sol1 = sol.wordBreak(s1, wordDict1)
print("Output:", sol1)
print("=".center(50, "="))

# Example 2
s2 = "applepenapple"
wordDict2 = ["apple", "pen"]
print("Example 2:")
print("Input s2:", s2)
sol2 = sol.wordBreak(s2, wordDict2)
print("Output:", sol2)
print("=".center(50, "="))

# Example 3
s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
print("Example 3:")
print("Input nums3:", s3)
sol3 = sol.wordBreak(s3, wordDict3)
print("Output:", sol3)
print("=".center(50, "="))