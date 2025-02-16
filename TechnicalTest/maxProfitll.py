from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the maximum profit to 0
        max_profit = 0
        
        # Iterate through the prices array starting from the second element
        for i in range(1, len(prices)):
            # If the current price is greater than the previous price, add the difference to the profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        # Return the maximum profit
        return max_profit

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
prices1 = [7, 1, 5, 3, 6, 4]
print("Example 1:")
print("Input:", prices1)
print("Output:", sol.maxProfit(prices1))
print("=".center(50,"="))

# Example 2
prices2 = [1, 2, 3, 4, 5]
print("Example 2:")
print("Input:", prices2)
print("Output:", sol.maxProfit(prices2))
print("=".center(50,"="))

# Example 3
prices3 = [7, 6, 4, 3, 1]
print("Example 3:")
print("Input:", prices3)
print("Output:", sol.maxProfit(prices3))
print("=".center(50,"="))
