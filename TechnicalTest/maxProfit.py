from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If there are no prices or only one price, no profit can be made
        if len(prices) < 2:
            return 0
        
        # Initialize minimum price seen so far and maximum profit achievable
        min_price = prices[0]  # The first day's price as our initial minimum
        max_profit = 0          # Initially assume no profit
        
        # Iterate through each day's price starting from the second day
        for current_price in prices[1:]:
            # Update minimum price if today's price is lower than previous minimums
            if current_price < min_price:
                min_price = current_price
            
            # Calculate potential profit by selling at today's price after buying at min_price
            potential_profit = current_price - min_price
            
            # Update max_profit if today's potential profit is higher than previous max profits
            if potential_profit > max_profit:
                max_profit = potential_profit
        
        return max_profit

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
prices1 = [7,1,5,3,6,4]
print("Example 1:")
print("Input prices:", prices1)
print("Output:", sol.maxProfit(prices1))

# Example 2
print("=".center(50,"="))
prices2 = [7,6,4,3,1]
print("Example 2:")
print("Input prices:", prices2)
print("Output:", sol.maxProfit(prices2))
print("=".center(50,"="))