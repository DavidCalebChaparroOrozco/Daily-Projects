# This function takes a string 's' and a dictionary of words 'wordDict',
# and returns all possible sentences formed by inserting spaces in 's' 
# such that each word in the sentence exists in the dictionary.
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        """        
        Approach:
        1. First check if the string can be broken into words using a helper function.
        2. Use memoization to store intermediate results and avoid recomputation.
        3. Perform recursive backtracking to find all possible word breaks.
        
        Args:
            s: Input string to be segmented
            wordDict: List of valid words
        Returns:
            List of all possible valid sentences
        """
        
        # Convert wordDict to a set for O(1) lookups
        word_set = set(wordDict)
        
        # Memoization dictionary to store already computed results
        memo = {}
        
        # Helper function that performs recursive backtracking to find all word breaks.
        def backtrack(s):
            """    
            Args:
                s: Current substring to process
            Returns:
                List of all possible word breaks for the current substring
            """
            # If result for this substring is already computed, return it
            if s in memo:
                return memo[s]
            
            # Base case: empty string has one solution - empty list
            if not s:
                return [""]
            
            results = []
            
            # Try all possible prefixes of the current string
            for i in range(1, len(s)+1):
                prefix = s[:i]
                # If prefix is a valid word
                if prefix in word_set:
                    # Recursively process the remaining string
                    for sentence in backtrack(s[i:]):
                        # Combine current prefix with sentences from the remaining string
                        if sentence:
                            results.append(prefix + " " + sentence)
                        else:
                            results.append(prefix)
            
            # Store the result in memo before returning
            memo[s] = results
            return results
        
        # First check if the string can be broken into words (optimization)
        def can_word_break(s):
            """
            Args:
                s: Input string
            Returns:
                Boolean indicating if word break is possible
            """
            n = len(s)
            dp = [False] * (n + 1)
            dp[0] = True  # empty string
            
            for i in range(1, n+1):
                for j in range(i):
                    if dp[j] and s[j:i] in word_set:
                        dp[i] = True
                        break
            return dp[n]
        
        # Early return if word break is not possible
        if not can_word_break(s):
            return []
        
        # Perform the backtracking to find all solutions
        return backtrack(s)

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
s1 = "catsanddog"
wordDict1 = ["cats", "and", "dog", "cat", "sand"]
print("Example 1:")
print("Input s1:", s1)
sol1 = sol.wordBreak(s1, wordDict1)
print("Output:", sol1)
print("=".center(50, "="))

# Example 2
s2 = "pineapplepenapple"
wordDict2 = ["apple", "pen", "applepen", "pine", "pineapple"]
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