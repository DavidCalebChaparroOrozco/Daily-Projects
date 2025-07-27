# Prints the 2D grid in a readable format.
def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

# Checks if the current position is valid for flood fill.
def is_valid(grid, x, y, target_color):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] == target_color

# Recursively fills all connected cells that match the target_color.
def flood_fill(grid, x, y, target_color, replacement_color):
    if not is_valid(grid, x, y, target_color) or target_color == replacement_color:
        return

    # Replace current cell with new color
    grid[x][y] = replacement_color

    # Recursive calls for 4 directions (up, down, left, right)
    flood_fill(grid, x + 1, y, target_color, replacement_color)
    flood_fill(grid, x - 1, y, target_color, replacement_color)
    flood_fill(grid, x, y + 1, target_color, replacement_color)
    flood_fill(grid, x, y - 1, target_color, replacement_color)


def main():
    # Example 2D grid (can be modified)
    grid = [
        ['R', 'R', 'G', 'G', 'G'],
        ['R', 'R', 'G', 'B', 'B'],
        ['G', 'G', 'G', 'B', 'B'],
        ['G', 'B', 'B', 'B', 'B'],
        ['G', 'G', 'B', 'B', 'B']
    ]

    print("Original Grid:")
    print_grid(grid)

    # Coordinates to start the flood fill
    x = int(input("Enter the row to start filling (0-based index): "))
    y = int(input("Enter the column to start filling (0-based index): "))

    # New color to apply
    new_color = input("Enter the new color (e.g., 'Y' for yellow): ").upper()

    # Get the target color to be replaced
    target_color = grid[x][y]

    # Apply flood fill
    flood_fill(grid, x, y, target_color, new_color)

    print("Grid after Flood Fill:")
    print_grid(grid)

if __name__ == "__main__":
    main()
