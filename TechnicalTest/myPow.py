class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case
        if n == 0:
            return 1
        
        # If n is negative, compute the positive power and take the reciprocal
        if n < 0:
            x = 1 / x
            n = -n
        
        # Recursive case: exponentiation by squaring
        half = self.myPow(x, n // 2)
        
        # If n is even
        if n % 2 == 0:
            return half * half
        else:
            # If n is odd
            return half * half * x

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
x1 = 2.00000
n1 = 10
print("Example 1:")
print("Input:", x1)
print("Output:", sol.myPow(x1, n1))
print("=".center(50,"="))

# Example 2
x2 = 2.10000
n2 = 3
print("Example 2:")
print("Input:", x2)
print("Output:", sol.myPow(x2, n2))
print("=".center(50,"="))

# Example 3
x3 = 2.00000
n3 = -2
print("Example 2:")
print("Input:", x3)
print("Output:", sol.myPow(x3, n3))
print("=".center(50,"="))