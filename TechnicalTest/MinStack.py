class MinStack:

    def __init__(self):
        # Initialize two stacks: one for the main elements and one for the minimum elements
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)
        # If the min_stack is empty or the value is less than or equal to the current minimum, push it onto the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the value from the main stack
        val = self.stack.pop()
        # If the popped value is the current minimum, pop it from the min_stack as well
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top element of the min_stack, which is the current minimum
        return self.min_stack[-1]

if __name__ == "__main__":
    # Create a MinStack instance
    min_stack = MinStack()

    # Operations according to the provided example
    operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    values = [[], [-2], [0], [-3], [], [], [], []]

    output = []
    for op, val in zip(operations, values):
        if op == "MinStack":
            output.append(None)
        elif op == "push":
            min_stack.push(val[0])
            output.append(None)
        elif op == "pop":
            min_stack.pop()
            output.append(None)
        elif op == "top":
            output.append(min_stack.top())
        elif op == "getMin":
            output.append(min_stack.getMin())

    # Print the results
    print("=".center(50, "="))
    print("Operations:", operations)
    print("Values:", values)
    print("Output:", output)
    print("=".center(50, "="))