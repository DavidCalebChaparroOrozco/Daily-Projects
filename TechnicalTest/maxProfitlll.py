from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If the prices array is empty, return 0
        if not prices:
            return 0
        
        # Initialize variables to track the maximum profit for the first and second transactions
        
        # first_buy: Maximum profit after the first buy (negative because we spend money)
        first_buy = -prices[0]  # We buy the stock on the first day
        # first_sell: Maximum profit after the first sell
        first_sell = 0          # We cannot sell on the first day
        # second_buy: Maximum profit after the second buy
        second_buy = -prices[0] # We buy the stock again (after selling the first time)
        # second_sell: Maximum profit after the second sell
        second_sell = 0         # We cannot sell on the first day
        
        # Iterate through the prices array starting from the second day
        for price in prices[1:]:
            # Update first_buy: Either keep the previous first_buy or buy the stock today
            first_buy = max(first_buy, -price)
            # Update first_sell: Either keep the previous first_sell or sell the stock today
            first_sell = max(first_sell, first_buy + price)
            # Update second_buy: Either keep the previous second_buy or buy the stock today (after first_sell)
            second_buy = max(second_buy, first_sell - price)
            # Update second_sell: Either keep the previous second_sell or sell the stock today
            second_sell = max(second_sell, second_buy + price)
        
        # The maximum profit is the value of second_sell
        return second_sell
    

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
prices1 = [3, 3, 5, 0, 0, 3, 1, 4]
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
