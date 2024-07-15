# You need to pack a set of items, with given values and sizes (such as weights or volumes), 
# into a container with a maximum capacity 

# Recursive function to solve the Knapsack problem.
def knapsack_recursive(weights, values, W, n):
    """
    :param weights: List of weights of the items
    :param values: List of values of the items
    :param W: Maximum weight capacity of the knapsack
    :param n: Number of items
    :return: Maximum value that can be obtained
    """
    # Base case: if no items are left or the capacity is 0
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than the knapsack capacity W, it cannot be included
    if weights[n-1] > W:
        return knapsack_recursive(weights, values, W, n-1)

    # Return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            values[n-1] + knapsack_recursive(weights, values, W-weights[n-1], n-1),
            knapsack_recursive(weights, values, W, n-1)
        )

# Dynamic programming function to solve the Knapsack problem.
def knapsack_dynamic(weights, values, W):
    """
    :param weights: List of weights of the items
    :param values: List of values of the items
    :param W: Maximum weight capacity of the knapsack
    :return: Maximum value that can be obtained
    """
    n = len(weights)
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table dp[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

# Example usage
weights = [1, 2, 3, 4]
values = [10, 20, 30, 40]
W = 5

print("Maximum value using recursion: ", knapsack_recursive(weights, values, W, len(weights)))
print("Maximum value using dynamic programming: ", knapsack_dynamic(weights, values, W))
