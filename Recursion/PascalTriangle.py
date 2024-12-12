# Import necessary libraries
import matplotlib.pyplot as plt

# Calculate the binomial coefficient C(n, k) using recursion.
def binomial_coefficient(n, k):
    """
    C(n, k) = n! / (k! * (n - k)!)
    This can also be defined recursively as:
    C(n, k) = C(n-1, k-1) + C(n-1, k)
    """
    # Base cases
    if k == 0 or k == n:
        return 1
    # Recursive case
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

# Generate the nth row of Pascal's Triangle.
def pascal_triangle_row(n):
    """    
    n: The row number (0-indexed)
    return: A list containing the elements of the nth row
    """
    row = []
    for k in range(n + 1):
        row.append(binomial_coefficient(n, k))
    return row

# Plot the given row of Pascal's Triangle.
def plot_pascal_triangle_row(row):
    """    
    row: List containing the elements of a specific row
    """
    plt.figure(figsize=(10, 5))
    
    # Create a bar plot for the row
    plt.bar(range(len(row)), row, color='skyblue')
    
    # Adding titles and labels
    plt.title(f'Pascal\'s Triangle Row {len(row) - 1}')
    plt.xlabel('Index')
    plt.ylabel('Value')
    
    # Annotate each bar with its value
    for i, value in enumerate(row):
        plt.text(i, value + 0.5, str(value), ha='center', va='bottom')
    
    plt.xticks(range(len(row)))
    plt.grid(axis='y')
    
    # Show the plot
    plt.show()

# Example usage
if __name__ == "__main__":
    n = 6 
    row = pascal_triangle_row(n)
    
    print(f"Pascal's Triangle Row {n}: {row}")
    
    plot_pascal_triangle_row(row)
