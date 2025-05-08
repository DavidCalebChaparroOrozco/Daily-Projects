# Count Distinct Paths in a Grid with Visualization

# Import necessary libraries
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

# Calculate the number of distinct paths in an n x m grid using combinatorics.
def count_distinct_paths(n, m):
    """
    Args:
        n: Number of rows in the grid (down moves)
        m: Number of columns in the grid (right moves)
    Returns:
        int: Number of distinct paths from (0,0) to (n,m)
    """
    # We need to make exactly (n+m) moves total: n down and m right
    # The number of unique ways to arrange these moves is (n+m choose n)
    
    # To avoid integer overflow and optimize calculation
    total = 1
    for i in range(1, n + m + 1):
        total *= i
    for i in range(1, n + 1):
        total //= i
    for i in range(1, m + 1):
        total //= i
    
    return total

# Alternative implementation using dynamic programming.
def count_paths_with_dp(n, m):
    """
    Args:
        n: Number of rows
        m: Number of columns 
    Returns:
        int: Number of distinct paths
    """
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = 1
    for j in range(m+1):
        dp[0][j] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[n][m]

# Visualize the grid and optionally highlight a specific path.
def visualize_grid(n, m, path=None):
    """    
    Args:
        n: Number of rows
        m: Number of columns
        path (list): List of coordinates representing a path (optional)
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Draw grid lines
    for i in range(n+1):
        ax.axhline(i, color='gray', linestyle='-', alpha=0.3)
    for j in range(m+1):
        ax.axvline(j, color='gray', linestyle='-', alpha=0.3)
    
    # Draw grid points
    for i in range(n+1):
        for j in range(m+1):
            ax.plot(j, n-i, 'o', markersize=10, color='blue', alpha=0.5)
    
    # Highlight start and end points
    ax.plot(0, n, 'o', markersize=15, color='green', label='Start (0,0)')
    ax.plot(m, 0, 'o', markersize=15, color='red', label=f'End ({n},{m})')
    
    # Draw path if provided
    if path:
        verts = [(col, n-row) for row, col in path]
        codes = [Path.MOVETO] + [Path.LINETO] * (len(verts)-1)
        path_obj = Path(verts, codes)
        patch = patches.PathPatch(path_obj, facecolor='none', edgecolor='orange', lw=2)
        ax.add_patch(patch)
        
        # Mark path points
        for row, col in path[1:-1]:
            ax.plot(col, n-row, 'o', markersize=12, color='orange')
    
    ax.set_xlim(-0.5, m+0.5)
    ax.set_ylim(-0.5, n+0.5)
    ax.set_aspect('equal')
    ax.set_xticks(range(m+1))
    ax.set_yticks(range(n+1))
    ax.set_xticklabels(range(m+1))
    ax.set_yticklabels(range(n, -1, -1))
    ax.set_xlabel('Columns')
    ax.set_ylabel('Rows')
    ax.set_title(f'{n}x{m} Grid - Possible Paths: {count_distinct_paths(n, m)}')
    ax.legend()
    ax.grid(True)
    
    plt.tight_layout()
    plt.show()

# Generate a simple sample path (alternating right and down moves).
def generate_sample_path(n, m):
    path = [(0, 0)]
    i, j = 0, 0
    while i < n or j < m:
        if j < m and (i == n or (j < m and (i+j) % 2 == 0)):
            j += 1
        else:
            i += 1
        path.append((i, j))
    return path

def main():
    print("Distinct Paths in a Grid Calculator with Visualization")
    print("=".center(50, '='))
    
    try:
        # Get grid dimensions from user
        n = int(input("Enter number of rows (n): "))
        m = int(input("Enter number of columns (m): "))
        
        if n < 0 or m < 0:
            print("Dimensions must be non-negative integers.")
            return
        
        print("\nCalculating using combinatorial approach...")
        paths = count_distinct_paths(n, m)
        print(f"Number of distinct paths: {paths}")
        
        print("\nCalculating using dynamic programming...")
        paths_dp = count_paths_with_dp(n, m)
        print(f"Number of distinct paths: {paths_dp}")
        
        print("\nGenerating visualization...")
        
        # Generate a sample path to visualize
        sample_path = generate_sample_path(n, m) if n > 0 and m > 0 else [(0,0)]
        visualize_grid(n, m, sample_path)
        
        print("\nNote: Both calculation methods should give the same result.")
        print("The visualization shows one sample path in orange.")
        
    except ValueError:
        print("Invalid input. Please enter integer values for dimensions.")

if __name__ == "__main__":
    main()