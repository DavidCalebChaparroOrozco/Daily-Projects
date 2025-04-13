# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import random

# Recursively generate landscape points using midpoint displacement algorithm.
def midpoint_displacement(start, end, roughness, vertical_scale, num_iterations):
    # Base case: return the start and end points
    if num_iterations == 0:
        return [start, end]
    
    # Calculate midpoint
    mid_x = (start[0] + end[0]) / 2
    mid_y = (start[1] + end[1]) / 2
    
    # Apply random displacement to the midpoint
    displacement = (random.random() - 0.5) * vertical_scale
    mid_y += displacement
    
    # Reduce vertical scale for next iteration to create finer details
    new_vertical_scale = vertical_scale * roughness
    
    # Recursively process the left and right segments
    left_segment = midpoint_displacement(
        start, (mid_x, mid_y), roughness, new_vertical_scale, num_iterations - 1
    )
    right_segment = midpoint_displacement(
        (mid_x, mid_y), end, roughness, new_vertical_scale, num_iterations - 1
    )
    
    # Combine segments, avoiding duplicate midpoint
    return left_segment[:-1] + right_segment

# Generate a complete landscape profile.
def generate_landscape(width, height, roughness=0.5, iterations=8):
    # Starting and ending points (flat line)
    start_point = (0, height/2)
    end_point = (width, height/2)
    
    # Initial vertical scale (controls maximum height variation)
    initial_vertical_scale = height * 0.5
    
    # Generate points recursively
    points = midpoint_displacement(
        start_point, end_point, roughness, initial_vertical_scale, iterations
    )
    
    # Unzip points into x and y coordinates
    x_coords, y_coords = zip(*points)
    
    return x_coords, y_coords

# Plot the generated landscape.
def plot_landscape(x_coords, y_coords):
    plt.figure(figsize=(12, 6))
    plt.fill_between(x_coords, y_coords, color='green', alpha=0.7)
    plt.plot(x_coords, y_coords, color='darkgreen', linewidth=1)
    plt.title('Recursively Generated Landscape')
    plt.xlabel('Distance')
    plt.ylabel('Elevation')
    plt.grid(True, alpha=0.3)
    plt.show()

def main():
    
    # Landscape parameters

    # Horizontal size of the landscape
    WIDTH = 1000       
    # Maximum height of the landscape
    HEIGHT = 500       
    # Roughness factor (0 = smooth, 1 = rough)
    ROUGHNESS = 0.55   
    # Number of recursive iterations
    ITERATIONS = 10    
    
    # Generate landscape
    x, y = generate_landscape(WIDTH, HEIGHT, ROUGHNESS, ITERATIONS)
    
    # Plot landscape
    plot_landscape(x, y)

if __name__ == "__main__":
    main()