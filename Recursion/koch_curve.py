# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Generate points for the Koch curve using recursion.
def koch_curve(start, end, depth):
    """    
    start: Starting point (x, y).
    end: Ending point (x, y).
    depth: Recursion depth.
    Returns:
    list: List of points (x, y) that make up the Koch curve.
    """
    if depth == 0:
        return [start, end]
    
    # Calculate the points dividing the line segment into thirds
    x1 = (2 * start[0] + end[0]) / 3
    y1 = (2 * start[1] + end[1]) / 3
    x2 = (start[0] + 2 * end[0]) / 3
    y2 = (start[1] + 2 * end[1]) / 3
    
    # Calculate the peak of the equilateral triangle
    peak_x = (start[0] + end[0]) / 2 - np.sqrt(3) * (end[1] - start[1]) / 6
    peak_y = (start[1] + end[1]) / 2 + np.sqrt(3) * (end[0] - start[0]) / 6
    
    # Recursively generate the Koch curve segments
    points = []
    points.extend(koch_curve(start, (x1, y1), depth - 1))
    points.append((peak_x, peak_y))
    points.extend(koch_curve((x2, y2), end, depth - 1))
    
    return points

# Plot the Koch curve for a given recursion depth.
def plot_koch_curve(depth):
    """    
    depth: Recursion depth for the Koch curve.
    """
    # Define the starting and ending points of the initial line segment
    start = (0, 0)
    end = (1, 0)
    
    # Generate the Koch curve points
    points = koch_curve(start, end, depth)
    
    # Extract x and y coordinates for plotting
    x_coords, y_coords = zip(*points)
    
    # Create the plot
    plt.figure(figsize=(10, 5))
    plt.plot(x_coords, y_coords, color='blue')
    
    # Set equal aspect ratio and title
    plt.axis('equal')
    plt.title(f'Koch Curve with Depth {depth}')
    
    # Show grid and plot
    plt.grid(True)
    plt.show()

# Set the recursion depth and plot the Koch curve
if __name__ == "__main__":
    # You can change this value to increase or decrease complexity
    depth = 4
    plot_koch_curve(depth)