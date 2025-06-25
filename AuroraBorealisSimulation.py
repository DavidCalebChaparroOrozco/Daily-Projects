# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap

# Create a custom colormap for aurora (greenish-blue-purple)
colors = [(0, 0, 0.2), (0, 0.5, 0.2), (0.2, 0.8, 0.4), 
            (0.5, 1, 0.7), (0.8, 0.7, 1), (1, 0.8, 1)]
aurora_cmap = LinearSegmentedColormap.from_list('aurora', colors)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 7))
# Set the background color to black
ax.set_facecolor("black")  
# Hide the axes
plt.axis("off")  

# Create the X and Y grid
x = np.linspace(-3, 3, 1200)
y = np.linspace(0, 5, 800)
X, Y = np.meshgrid(x, y)

# Aurora wave pattern generator with more complexity
def aurora_pattern(frame):
    # Time-dependent parameters
    t = frame * 0.05
    y_scale = 0.5 + 0.2 * np.sin(t * 0.3)
    
    # Multiple moving waves with different frequencies
    wave1 = np.sin(2 * X + t) * np.exp(-Y * (0.8 + 0.1 * np.sin(t * 0.2)))
    wave2 = 0.7 * np.cos(3.5 * X - t * 0.7 + Y * 1.5) * np.exp(-Y * y_scale)
    wave3 = 0.5 * np.sin(5 * X + t * 0.3 + Y * 0.7) * np.exp(-Y * 0.6)
    wave4 = 0.3 * np.cos(1.5 * X - t * 0.5 + Y * 2) * np.exp(-Y * 0.4)
    
    # Combine waves with different weights
    pattern = (wave1 + wave2 + wave3 + wave4) * np.exp(-Y * 0.3)
    
    # Add some noise for texture
    noise = np.random.randn(*X.shape) * 0.05 * np.exp(-Y * 0.8)
    
    return pattern + noise

# Display initial image
initial_data = aurora_pattern(0)
img = ax.imshow(initial_data, extent=[-3, 3, 0, 5],
                origin='lower', cmap=aurora_cmap, alpha=0.95,
                vmin=-2, vmax=2)

# Add some stars in the background
stars_x = np.random.uniform(-3, 3, 200)
stars_y = np.random.uniform(0, 5, 200)
stars_size = np.random.uniform(0.01, 0.2, 200)
stars = ax.scatter(stars_x, stars_y, s=stars_size, c='white', alpha=0.8)

# Update function for the animation
def update(frame):
    Z = aurora_pattern(frame)
    img.set_array(Z)
    
    # Make stars twinkle slightly
    if frame % 5 == 0:
        stars.set_alpha(np.random.uniform(0.6, 0.9, size=len(stars_x)))
    
    return [img, stars]

# Create animation
ani = animation.FuncAnimation(fig, update, frames=300, interval=40, blit=True)

plt.tight_layout()
plt.show()