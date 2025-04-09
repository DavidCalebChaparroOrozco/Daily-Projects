# Import necessary libraries
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import random
import math

# Define the Circle class with overlap detection
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def overlaps(self, other):
        distance = math.hypot(self.x - other.x, self.y - other.y)
        return distance < (self.radius + other.radius)

# Recursive generator to yield circles one by one
def generate_circles(x, y, radius, depth):
    if depth == 0:
        return
    new_circle = Circle(x, y, radius)
    if is_valid(new_circle):
        yield new_circle
        for _ in range(8):
            angle = random.uniform(0, 2 * math.pi)
            new_radius = radius * random.uniform(0.3, 0.6)
            new_x = x + (radius + new_radius) * math.cos(angle)
            new_y = y + (radius + new_radius) * math.sin(angle)
            yield from generate_circles(new_x, new_y, new_radius, depth - 1)

# Check if circle is valid (non-overlapping)
def is_valid(circle):
    for c in drawn_circles:
        if circle.overlaps(c):
            return False
    return True

# Initialize figure
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')  # Hide axis

# Global storage for drawn circles
drawn_circles = []
circle_patches = []

# Create the generator
circle_gen = generate_circles(50, 50, 15, depth=5)

# Animation function
def update(frame):
    try:
        new_circle = next(circle_gen)
        drawn_circles.append(new_circle)
        patch = patches.Circle((new_circle.x, new_circle.y), new_circle.radius, 
                            fill=False, edgecolor='black', linewidth=1)
        ax.add_patch(patch)
        circle_patches.append(patch)
    except StopIteration:
        pass
    return circle_patches

# Create the animation
ani = FuncAnimation(fig, update, interval=50, blit=False)

# Show the animation
plt.show()
