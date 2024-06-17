# Given a string `s` and an array of strings `words`, find all starting indices of substring(s) in `s` 
# that is a concatenation of each word in `words` exactly once and without any intervening characters.

# Importing necessary libraries
from typing import List
from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_length = len(words[0])
        num_words = len(words)
        substring_length = word_length * num_words
        
        # Build the frequency map of words
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        result = []
        
        # Traverse the string with a sliding window of the total substring length
        for i in range(len(s) - substring_length + 1):
            seen_words = defaultdict(int)
            j = 0
            while j < num_words:
                word_start = i + j * word_length
                word = s[word_start:word_start + word_length]
                if word in word_count:
                    seen_words[word] += 1
                    if seen_words[word] > word_count[word]:
                        break
                else:
                    break
                j += 1
            
            if j == num_words:
                result.append(i)
        
        return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
print("Example 1:", sol.findSubstring(s1, words1))
print("=".center(50,"="))

# Example 2
s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
print("Example 2:", sol.findSubstring(s2, words2))
print("=".center(50,"="))

# Example 3
s3 = "barfoofoobarthefoobarman"
words3 = ["bar","foo","the"]
print("Example 3:", sol.findSubstring(s3, words3))
print("=".center(50,"="))