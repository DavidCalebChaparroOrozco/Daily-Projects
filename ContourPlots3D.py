# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Generate 1D arrays for x and y, ranging from -5 to 5 with 100 points each
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Create 2D grid coordinates from the 1D arrays
x, y = np.meshgrid(x,y)
z = x * y
# z = np.sin(x) * np.cos(y)
# z = x**2 + y ** 2
# z = - x**2 - y ** 2

# Create a figure with a specific size
fig = plt.figure(figsize=(14,6))

# Add a 3D subplot
ax = fig.add_subplot(121, projection ="3d")

# Plot a 3D surface plot
ax.plot_surface(x, y, z, cmap="viridis")
ax.set_title("3D Plot")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.set_zlabel("Z-Axis")

# Add a 2D subplot
ax2 = fig.add_subplot(122)

# Plot a 2D surface plot
# contour = ax2.contour(x, y, z, cmap="viridis")
contour = ax2.contourf(x, y, z, cmap="viridis")
fig.colorbar(contour, ax=ax2, shrink=0.5, aspect=5)
ax2.set_title("Contour Plot")
ax2.set_xlabel("X-Axis")
ax2.set_ylabel("Y-Axis")

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()