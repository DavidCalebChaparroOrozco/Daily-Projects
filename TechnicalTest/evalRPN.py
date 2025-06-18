class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                # It's an operator: pop two operands
                b = stack.pop()
                a = stack.pop()
                # Perform the operation based on the operator
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Division truncates toward zero
                    stack.append(int(a / b))
            else:
                # It's a number: push to stack
                stack.append(int(token))
        # The remaining element is the result
        return stack.pop()
    
# Example usage:
sol = Solution()

# Example 1
print("=".center(50, "="))
token1 = ["2","1","+","3","*"]
print("Example 1:")
print("Input:", token1)
print("Output:", sol.evalRPN(token1))
print("=".center(50, "="))

# Example 2
token2 = ["4","13","5","/","+"]
print("Example 2:")
print("Input:", token2)
print("Output:", sol.evalRPN(token2))
print("=".center(50, "="))

# Example 3
token3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print("Example 3:")
print("Input:", token3)
print("Output:", sol.evalRPN(token3))
print("=".center(50, "="))