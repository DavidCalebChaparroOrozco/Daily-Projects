# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Plot a linear function y = mx + b.
def plot_linear_function(slope, intercept):
    x = np.linspace(-10, 10, 100)  
    y = slope * x + intercept
    
    plt.plot(x, y, label=f'y = {slope}x + {intercept}')
    plt.title('Linear Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5, ls='--')  
    plt.axvline(0, color='black',linewidth=0.5, ls='--') 
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()

# Plot a quadratic function y = ax^2 + bx + c.
def plot_quadratic_function(a, b, c):
    x = np.linspace(-10, 10, 100)  
    y = a * x**2 + b * x + c
    
    plt.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
    plt.title('Quadratic Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5, ls='--')  
    plt.axvline(0, color='black',linewidth=0.5, ls='--')  
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()

# Plot a sine wave.
def plot_sine_wave():
    x = np.linspace(0, 2 * np.pi, 100) 
    y = np.sin(x)
    
    plt.plot(x, y, label='y = sin(x)')
    plt.title('Sine Wave')
    plt.xlabel('x (radians)')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5, ls='--')  # x-axis
    plt.axvline(0, color='black',linewidth=0.5, ls='--')  # y-axis
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()

# Main function to execute the plotting of different functions.
def main():
    
    print("Plotting Linear Function:")
    plot_linear_function(2, 3)

    print("Plotting Quadratic Function:")
    plot_quadratic_function(1, -2, -3)

    print("Plotting Sine Wave:")
    plot_sine_wave()

if __name__ == "__main__":
    main()
