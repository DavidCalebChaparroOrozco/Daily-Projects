# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Function to compute the Mandelbrot sequence
def mandelbrot(c, max_iter):
    # Initialize z to zero
    z = 0  
    for n in range(max_iter):
        if abs(z) > 3:
            return n 
        z = z * z + c
    # Return max_iter if the point is in the set
    return max_iter  

# Function to generate the Mandelbrot set
def mandelbrot_set(x_min, x_max, y_min, y_max, width, height, max_iter):
    # Create a linear space for the real part
    x = np.linspace(x_min, x_max, width)  
    # Create a linear space for the imaginary part
    y = np.linspace(y_min, y_max, height)  
    # Initialize the array to store the set
    m_set = np.zeros((height, width))  

    # Iterate over each point in the complex plane
    for i in range(height):
        for j in range(width):
            # Create a complex number from the grid
            c = complex(x[j], y[i])  
            # Compute the Mandelbrot value
            m_set[i, j] = mandelbrot(c, max_iter)  

    # Return the computed set
    return m_set  

# Define the parameters for the Mandelbrot set
x_min, x_max, y_min, y_max = -2.0, 1.0, -1.5, 1.5
width, height = 1000, 1000
max_iter = 100

# Generate the Mandelbrot set image
mandelbrot_image = mandelbrot_set(x_min, x_max, y_min, y_max, width, height, max_iter)

# Plot the Mandelbrot set
plt.imshow(mandelbrot_image, extent=[x_min, x_max, y_min, y_max], cmap='hot')
plt.colorbar()
plt.title("Mandelbrot by David Caleb")
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.show()
