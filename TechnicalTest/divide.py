class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge cases for overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values for simplicity
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        # The idea is to subtract the divisor from the dividend
        # but doing so in a more efficient way using bitwise shifts
        while dividend >= divisor:
            # Initialize power and value
            power = 1
            value = divisor
            
            # Double the value and power until value is greater than dividend
            while value <= (dividend >> 1):
                value <<= 1
                power <<= 1
            
            # Subtract the largest multiple of divisor
            dividend -= value
            quotient += power
        
        # Apply the sign to the result
        if negative:
            quotient = -quotient
        
        # Clamp the result to the 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
dividend1 = 10
divisor1 = 3
print("Example 1:", sol.divide(dividend1, divisor1))
print("=".center(50,"="))

# Example 2
dividend2 = 7
divisor2 = -3
print("Example 2:", sol.divide(dividend2, divisor2))  
print("=".center(50,"="))