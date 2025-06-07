import math
from collections import defaultdict

class Solution:
    # Function to find the maximum number of points that lie on the same straight line
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            # Any two points lie on the same line
            return n  
        
        # At least one point
        max_points = 1  
        
        for i in range(n):
            x1, y1 = points[i]
            slope_counts = defaultdict(int)
            current_max = 0
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                
                # Handle vertical and horizontal lines
                if dx == 0:
                    # Vertical line: slope is infinity, represented as (1, 0)
                    key = (1, 0)
                elif dy == 0:
                    # Horizontal line: slope is 0, represented as (0, 1)
                    key = (0, 1)
                else:
                    # Simplify the slope using GCD to avoid floating-point precision issues
                    gcd_val = math.gcd(abs(dx), abs(dy))
                    dx //= gcd_val
                    dy //= gcd_val
                    # Ensure consistent representation of the slope
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    # Using (dy, dx) to represent slope dy/dx
                    key = (dy, dx)  
                
                slope_counts[key] += 1
                current_max = max(current_max, slope_counts[key])
            
            # Update the global maximum points on a line
            
            # +1 to include the current point (points[i])
            max_points = max(max_points, current_max + 1)  
        
        return max_points

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
points1 = [[1,1],[2,2],[3,3]]
print("Example 1:")
print("Input:", points1)
print("Output:", sol.maxPoints(points1))
print("=".center(50, "="))

# Example 2
points2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print("Example 2:")
print("Input:", points2)
print("Output:", sol.maxPoints(points2))  
print("=".center(50, "="))