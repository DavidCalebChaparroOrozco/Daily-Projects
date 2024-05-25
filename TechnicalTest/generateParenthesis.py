# Given n pairs of parentheses, write a function to generate all combinations 
# of well-formed parentheses.

class Solution(object):
    def generateParenthesis(self, n):
        def backtrack(current, open_count, close_count):
            # Base case: If the current string has reached the maximum length (2 * n)
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # If we can still add an open parenthesis, add it and recurse
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # If we can add a close parenthesis without breaking the well-formed property,
            # add it and recurse
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        # This will store all the well-formed combinations
        result = []
        # Start the backtracking with an empty string and 0 open and close counts
        backtrack("", 0, 0)
        return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
num1 = 3
print("Example 1:")
print("Input:", num1)
print("Example 1:", sol.generateParenthesis(num1))
print("=".center(50,"="))

# Example 2
num2 = 1
print("Example 2:")
print("Input:", num2)
print("Example 2:", sol.generateParenthesis(num2))  
print("=".center(50,"="))