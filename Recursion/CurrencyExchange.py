def optimal_change(coins, amount):
    # Function to find all possible combinations of coins
    def combinations(coins, amount, result, current_combination):
        if amount == 0:
            result.append(current_combination.copy())
            return
        if amount < 0:
            return
        
        for coin in coins:
            current_combination.append(coin)
            combinations(coins, amount - coin, result, current_combination)
            current_combination.pop()

    # Function to find the optimal combination with the least number of coins
    def best_combination(coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        coins_used = [[] for _ in range(amount + 1)]

        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    coins_used[i] = coins_used[i - coin] + [coin]

        return coins_used[amount] if dp[amount] != float('inf') else None

    result_combinations = []
    combinations(coins, amount, result_combinations, [])
    
    optimal_comb = best_combination(coins, amount)

    return {
        "all_combinations": result_combinations,
        "optimal_combination": optimal_comb
    }

# Example usage with US coins (1 cent, 5 cents, 10 cents, 25 cents)
us_coins = [1, 5, 10, 25]
us_amount = 30

# Example usage with Colombian coins (100 pesos, 200 pesos, 500 pesos)
col_coins = [100, 200, 500]
col_amount = 800

# Get results for US and Colombian coins
result_us = optimal_change(us_coins, us_amount)
result_col = optimal_change(col_coins, col_amount)

# Print the results
print("Results for USD:", result_us)
print("Results for COP:", result_col)
