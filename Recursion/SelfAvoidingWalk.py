import random

# Define the directions for movement: up, down, left, right
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Check if the next move is within the grid bounds and hasn't been visited.
def is_valid_move(x, y, grid):
    n = len(grid)
    return 0 <= x < n and 0 <= y < n and not grid[x][y]

# Recursive function to perform a self-avoiding walk.
def self_avoiding_walk(x, y, grid, steps):
    # Mark the current position as visited
    grid[x][y] = True
    
    # If we've taken enough steps, we can stop
    if steps == len(grid) * len(grid[0]):
        return True
    
    # Store valid directions that can be used for movement
    valid_moves = []
    
    for dx, dy in DIRECTIONS:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(new_x, new_y, grid):
            valid_moves.append((new_x, new_y))
    
    # If no valid moves left, the walk ends here (failure)
    if not valid_moves:
        grid[x][y] = False  # Backtrack by marking this as unvisited
        return False
    
    # Shuffle directions to explore randomly
    random.shuffle(valid_moves)
    
    for new_x, new_y in valid_moves:
        if self_avoiding_walk(new_x, new_y, grid, steps + 1):
            return True
    
    # Backtrack if none of the moves lead to a solution
    grid[x][y] = False
    return False

# Initiates the self-avoiding walk on an n x n grid.
def initiate_walk(grid_size):
    # Initialize a grid of size n x n where False indicates unvisited positions
    grid = [[False for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Start the walk from the middle of the grid
    start_x, start_y = grid_size // 2, grid_size // 2
    success = self_avoiding_walk(start_x, start_y, grid, 1)
    
    if success:
        print("Self-avoiding walk completed successfully!")
    else:
        print("Walk failed (got stuck).")
    
    return grid

# Example of running the self-avoiding walk on a 5x5 grid
grid_size = 5
result_grid = initiate_walk(grid_size)

# Display the final grid (True = visited, False = unvisited)
for row in result_grid:
    print(row)
