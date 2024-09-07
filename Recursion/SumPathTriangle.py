# Function to find the maximum sum path from top to bottom in a triangle

# Recursive function to find the maximum sum path in a triangle.
def max_sum_path(triangle, row, col, n):
    """
    Parameters:
    triangle: The list of lists representing the triangle.
    row : The current row in the triangle.
    col : The current column in the triangle.
    n : The total number of rows in the triangle.

    Returns:
    int: The maximum sum path from the current element to the base.
    """
    # Base case: If we are at the last row, return the current element
    if row == n - 1:
        return triangle[row][col]

    # Recursive case: Move to the next row and choose the maximum path
    # We can go to the element directly below or the element below-right
    left_path = max_sum_path(triangle, row + 1, col, n)
    right_path = max_sum_path(triangle, row + 1, col + 1, n)

    # Return the current element value plus the maximum of the two possible paths
    return triangle[row][col] + max(left_path, right_path)

# Function to start the recursion from the top of the triangle

# Function to initiate the recursive calculation for the maximum sum path in a triangle.
def find_max_sum(triangle):
    """
    Parameters:
    triangle: The list of lists representing the triangle.

    Returns:
    int: The maximum sum path from the top to the base.
    """
    if not triangle:
        return 0

    # Start the recursion from the top of the triangle (0, 0)
    return max_sum_path(triangle, 0, 0, len(triangle))

# Example usage
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

max_sum = find_max_sum(triangle)
print(f"The maximum sum path in the triangle is: {max_sum}")
