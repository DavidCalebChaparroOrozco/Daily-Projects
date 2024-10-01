class Solution:
    def climbStairs(self, n: int) -> int:
        # If there is only 1 or 2 steps, the number of ways to reach the top is the same as the number of steps
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize the first two values of the Fibonacci sequence
        # Number of ways to reach step 1
        first = 1  
        # Number of ways to reach step 2
        second = 2  
        
        # Iterate from the 3rd step to the nth step
        for i in range(3, n + 1):
            # Current step is the sum of the previous two steps
            current = first + second  
            # Move to the next step in the sequence
            first = second  
            # Update the next step to the current value
            second = current  
        
        # Return the total number of ways to reach the nth step
        return second

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
n1 = 2
print("Example 1:")
print("Input:", n1)
print("Output:", sol.climbStairs(n1))
print("=".center(50,"="))

# Example 2
n2 = 3
print("Example 2:")
print("Input:", n2)
print("Output:", sol.climbStairs(n2))
print("=".center(50,"="))