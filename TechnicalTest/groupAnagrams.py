from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold the list of anagrams with sorted tuple of characters as keys
        anagrams = defaultdict(list)
        
        for word in strs:
            # Sort the word and use it as a key
            sorted_word = ''.join(sorted(word))
            # Append the original word to the list corresponding to the sorted key
            anagrams[sorted_word].append(word)
        
        # Return the values of the dictionary which are lists of grouped anagrams
        return list(anagrams.values())

# Example usage
solution = Solution()

# Example 1
print("=".center(50,"="))
print("Example 1:")
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Input:", strs1)
print("Output:", solution.groupAnagrams(strs1))
print("=".center(50,"="))

# Example 2
print("Example 2:")
strs2 = [""]
print("Input:", strs2)
print("Output:", solution.groupAnagrams(strs2))
print("=".center(50,"="))

# Example 3
print("Example 3:")
strs3 = ["a"]
print("Input:", strs3)
print("Output:", solution.groupAnagrams(strs3))
print("=".center(50,"="))