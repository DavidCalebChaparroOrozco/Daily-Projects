# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# Generates random points within specified limits.
def generate_random_points(num_points, x_limits, y_limits):
    x_coords = np.random.uniform(x_limits[0], x_limits[1], num_points)
    y_coords = np.random.uniform(y_limits[0], y_limits[1], num_points)
    return np.column_stack((x_coords, y_coords))

# Recursively generates Voronoi diagrams by dividing the space into regions.
def recursive_voronoi(points, depth, x_limits, y_limits):
    if depth == 0 or len(points) < 2:
        return
    
    # Generate Voronoi diagram for the current set of points
    vor = Voronoi(points)
    
    # Plot the Voronoi diagram
    fig, ax = plt.subplots()
    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='black')
    ax.set_xlim(x_limits)
    ax.set_ylim(y_limits)
    ax.set_title(f"Recursive Voronoi Diagram - Depth {depth}")
    plt.show()
    
    # Process each region
    for region_index in vor.point_region:
        region = vor.regions[region_index]
        
        # Skip invalid or empty regions
        if not region or -1 in region:
            continue
        
        # Get the vertices of the region
        vertices = vor.vertices[region]
        
        # Define the bounding box of the region
        x_min, x_max = np.min(vertices[:, 0]), np.max(vertices[:, 0])
        y_min, y_max = np.min(vertices[:, 1]), np.max(vertices[:, 1])

        # Skip degenerate regions (zero width or height)
        if x_max - x_min <= 0 or y_max - y_min <= 0:
            continue
        
        # Generate new points within the region
        new_points = generate_random_points(5, (x_min, x_max), (y_min, y_max))
        
        # Recursively generate Voronoi diagrams for the new points
        recursive_voronoi(new_points, depth - 1, x_limits, y_limits)

def main():
    # Define the initial parameters
    num_points = 10
    x_limits = (0, 10)
    y_limits = (0, 10)
    recursion_depth = 3
    
    # Generate initial random points
    initial_points = generate_random_points(num_points, x_limits, y_limits)
    
    # Start the recursive Voronoi diagram generation
    recursive_voronoi(initial_points, recursion_depth, x_limits, y_limits)

if __name__ == "__main__":
    main()
