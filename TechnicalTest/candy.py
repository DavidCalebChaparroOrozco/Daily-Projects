from typing import List

class Solution:
# Calculates the minimum number of candies needed to distribute to children based on their ratings.
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        
        # Initialize each child with 1 candy
        candies = [1] * n
        
        # Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Sum all candies
        return sum(candies)
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
ratings1 = [1, 0, 2]
print("Example 1:")
print("Input ratings1:", ratings1)
sol1 = sol.candy(ratings1)
print("Output:", sol1)
print("=".center(50, "="))

# Example 2
ratings2 = [1, 2, 2]
print("Example 2:")
print("Input ratings2:", ratings2)
sol2 = sol.candy(ratings2)
print("Output:", sol2)
print("=".center(50, "="))