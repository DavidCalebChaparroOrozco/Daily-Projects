# Calculate the nth Fibonacci number using recursion.
def fibonacci(n):
    """    
    n (int): The position in the Fibonacci sequence to calculate.
    
    Returns:
    int: The nth Fibonacci number.
    """
    # Base case: return n if it is 0 or 1
    if n <= 1:
        return n
    
    # Recursive case: sum of the two preceding numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
if __name__ == "__main__":
    # Change this value to compute a different Fibonacci number
    position = 10
    result = fibonacci(position)
    print(f"The {position}th Fibonacci number is: {result}")