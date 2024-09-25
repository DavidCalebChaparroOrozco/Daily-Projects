class Solution:
    def mySqrt(self, x: int) -> int:
        # Edge case: if x is 0 or 1, return x itself as the square root
        if x < 2:
            return x
        
        # Initialize left and right pointers for binary search
        left, right = 1, x // 2
        
        while left <= right:
            # Find the middle element
            mid = (left + right) // 2
            # Calculate mid squared
            mid_squared = mid * mid
            
            # Check if we have found the exact square root
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                # If mid^2 is less than x, move the left pointer to the right of mid
                left = mid + 1
            else:
                # If mid^2 is greater than x, move the right pointer to the left of mid
                right = mid - 1
        
        # When the loop exits, right will be the integer part of the square root of x
        return right

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
x1 = 4
print("Example 1:")
print("Input:", x1)
print("Output:", sol.mySqrt(x1))
print("=".center(50,"="))

# Example 2
x2 = 8
print("Example 1:")
print("Input:", x2)
print("Output:", sol.mySqrt(x2))
print("=".center(50,"="))