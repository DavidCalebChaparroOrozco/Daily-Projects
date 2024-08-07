# Importing necessary libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Function to draw the recursive tree
def draw_tree(x, y, angle, length, depth, max_depth, ax):
    if depth == max_depth:
        return
    
    # Calculate the end points of the current branch
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)
    
    # Draw the current branch
    line, = ax.plot([x, x_end], [y, y_end], color='green', lw=2)
    
    # Recursively draw the left and right branches
    draw_tree(x_end, y_end, angle - np.pi / 6, length * 0.7, depth + 1, max_depth, ax)
    draw_tree(x_end, y_end, angle + np.pi / 6, length * 0.7, depth + 1, max_depth, ax)
    
    return line

# Animation function to update each frame
def update(frame, ax, initial_depth, max_depth):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 2)
    draw_tree(0, 0, np.pi / 2, 0.3, 0, initial_depth + frame, ax)

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')

# Create the animation
initial_depth = 0 
max_depth = 10
ani = animation.FuncAnimation(fig, update, frames=max_depth, fargs=(ax, initial_depth, max_depth), interval=1000, repeat=False)

# Display the animation
plt.show()
