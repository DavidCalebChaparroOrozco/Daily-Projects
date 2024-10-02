# Function to perform Depth-First Search (DFS) to mark all cells of the current island
def dfs(grid, row, col, rows, cols):
    """
    Recursive function to mark all cells of an island as visited using DFS.
    
    Parameters:
    grid (list): The 2D grid representing water (0) and land (1).
    row (int): The current row index.
    col (int): The current column index.
    rows (int): Total number of rows in the grid.
    cols (int): Total number of columns in the grid.
    """
    # Check if the current cell is out of bounds or not land (water or already visited)
    if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
        return
    
    # Mark the current cell as visited by setting it to 0
    grid[row][col] = 0

    # Recursively call DFS in all 8 possible directions (up, down, left, right, and diagonals)
    dfs(grid, row - 1, col, rows, cols)    # Up
    dfs(grid, row + 1, col, rows, cols)    # Down
    dfs(grid, row, col - 1, rows, cols)    # Left
    dfs(grid, row, col + 1, rows, cols)    # Right
    dfs(grid, row - 1, col - 1, rows, cols) # Top-left diagonal
    dfs(grid, row - 1, col + 1, rows, cols) # Top-right diagonal
    dfs(grid, row + 1, col - 1, rows, cols) # Bottom-left diagonal
    dfs(grid, row + 1, col + 1, rows, cols) # Bottom-right diagonal

# Function to count the number of islands in the grid
def count_islands(grid):
    """
    Function to count the number of islands in the grid using DFS.
    
    Parameters:
    grid (list): The 2D grid representing water (0) and land (1).
    
    Returns:
    int: The total number of islands found in the grid.
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    island_count = 0

    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # If the cell is land (1), it's the start of a new island
            if grid[row][col] == 1:
                # Perform DFS to mark all connected land cells as visited
                dfs(grid, row, col, rows, cols)
                # Increment the island count
                island_count += 1
    
    return island_count

# Example usage
grid = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

total_islands = count_islands(grid)
print(f"The number of islands in the grid is: {total_islands}")
