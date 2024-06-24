# Given a string containing just the characters '(' and ')', 
# return the length of the longest valid (well-formed) parentheses substring

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize a stack with a base value of -1
        stack = [-1]
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                # Push the index of the '(' onto the stack
                stack.append(i)
            else:
                # Pop the topmost element
                stack.pop()
                if not stack:
                    # If the stack is empty, push the current index onto the stack
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring
                    max_length = max(max_length, i - stack[-1])

        return max_length

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
s1 = "(()"
print("Example 1:")
print("Input:", s1)
print("Output:", sol.longestValidParentheses(s1))
print("=".center(50,"="))

# Example 2
s2 = ")()())"
print("Example 2:")
print("Input:", s2)
print("Output:", sol.longestValidParentheses(s2))
print("=".center(50,"="))

# Example 3
s3 = ""
print("Example 2:")
print("Input:", s3)
print("Output:", sol.longestValidParentheses(s3))
print("=".center(50,"="))