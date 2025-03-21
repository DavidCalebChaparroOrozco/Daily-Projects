from typing import List

class Solution:
    # Return all possible palindrome partitioning of the string s.
    def partition(self, s: str) -> List[List[str]]:
        # To store all valid partitions
        result = []  
        # Start DFS from the first character
        self.dfs(s, 0, [], result)  
        return result

    # Depth-First Search to find all valid palindrome partitions.
    def dfs(self, s: str, start: int, path: List[str], result: List[List[str]]) -> None:
        # If we've reached the end of the string, add the current path to the result
        if start == len(s):
            # Use a copy of the path to avoid reference issues
            result.append(path[:])  
            return
        
        # Explore all possible partitions starting from the current index
        for end in range(start + 1, len(s) + 1):
            # Get the current substring
            substring = s[start:end]  
            # Check if it's a palindrome
            if self.is_palindrome(substring):  
                # Add it to the current path
                path.append(substring)  
                # Recur for the remaining string
                self.dfs(s, end, path, result)  
                # Backtrack and remove the last substring to explore other options
                path.pop()  

    # Check if a string is a palindrome.
    def is_palindrome(self, s: str) -> bool:
        # Compare the string with its reverse
        return s == s[::-1]  


# Example usage
sol = Solution()

# Example 1
print("=".center(50, "="))
print("Example 1:")
s1 = "aab"
print("Input:", s1)
print("Output:", sol.partition(s1))

# Example 2
print("=".center(50, "="))
print("Example 2:")
s2 = "a"
print("Input:", s2)
print("Output:", sol.partition(s2))
print("=".center(50, "="))