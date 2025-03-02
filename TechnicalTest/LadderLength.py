from typing import List, Dict, Set
from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # Convert wordList to a set for O(1) lookups
        wordSet = set(wordList)
        
        # If the endWord is not in the wordList, no transformation is possible
        if endWord not in wordSet:
            return []
        
        # Initialize a queue for BFS
        queue = deque()
        queue.append((beginWord, [beginWord]))  # Each element in the queue is a tuple (current_word, path)
        
        # Initialize a set to keep track of visited words to avoid cycles
        visited = set()
        visited.add(beginWord)
        
        # Initialize a dictionary to store the shortest paths to each word
        shortest_paths = defaultdict(list)
        shortest_paths[beginWord] = [[beginWord]]
        
        # Initialize a flag to indicate if we have found the endWord
        found = False
        
        # Perform BFS
        while queue and not found:
            level_size = len(queue)
            level_visited = set()  # Keep track of words visited at the current level
            
            for _ in range(level_size):
                current_word, path = queue.popleft()
                
                # Generate all possible transformations of the current word
                for i in range(len(current_word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == current_word[i]:
                            continue
                        next_word = current_word[:i] + c + current_word[i+1:]
                        
                        # If the next_word is the endWord, we have found a valid path
                        if next_word == endWord:
                            found = True
                            shortest_paths[endWord].append(path + [next_word])
                        
                        # If the next_word is in the wordSet and not visited in the current level
                        if next_word in wordSet and next_word not in visited:
                            if next_word not in level_visited:
                                level_visited.add(next_word)
                                queue.append((next_word, path + [next_word]))
                            shortest_paths[next_word].append(path + [next_word])
            
            # Mark all words visited at this level as visited
            visited.update(level_visited)
        
        # Return the shortest paths to the endWord
        return shortest_paths[endWord]

# Example usage:
sol = Solution()

# Example 1
print("=".center(50, "="))
beginWord1 = "hit"
endWord1 = "cog"
wordList1 = ["hot","dot","dog","lot","log","cog"]
print("Example 1:")
print("Input:", beginWord1, endWord1, wordList1)
print("Output:", sol.findLadders(beginWord1, endWord1, wordList1))
print("=".center(50, "="))

# Example 2
beginWord2 = "hit"
endWord2 = "cog"
wordList2 = ["hot","dot","dog","lot","log"]
print("Example 2:")
print("Input:", beginWord2, endWord2, wordList2)
print("Output:", sol.findLadders(beginWord2, endWord2, wordList2))
print("=".center(50, "="))