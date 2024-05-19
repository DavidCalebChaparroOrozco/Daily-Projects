# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        # Dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        # Iterate over each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop from the stack or use a dummy value if the stack is empty
                top_element = stack.pop() if stack else '#'
                
                # If the bracket does not match the expected opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it is an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty at the end, all brackets are closed correctly
        return not stack

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
s1 = "()"
print("Example 1:", sol.isValid(s1))
print("=".center(50,"="))

# Example 2
s2 = "()[]{}"
print("Example 2:", sol.isValid(s2))  
print("=".center(50,"="))

# Example 3
s3 = "(]"
print("Example 3:", sol.isValid(s3))  
print("=".center(50,"="))