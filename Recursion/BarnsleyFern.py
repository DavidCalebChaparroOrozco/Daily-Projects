# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import ttk
import random

# Generate Barnsley Fern points with customizable parameters
def barnsley_fern(iterations, probabilities=None, coefficients=None):
    # Default parameters (standard Barnsley Fern)
    if probabilities is None:
        probabilities = [0.01, 0.85, 0.07, 0.07]
    if coefficients is None:
        coefficients = [
            [0, 0, 0, 0.16, 0, 0],
            [0.85, 0.04, -0.04, 0.85, 0, 1.6],
            [0.2, -0.26, 0.23, 0.22, 0, 1.6],
            [-0.15, 0.28, 0.26, 0.24, 0, 0.44]
        ]
    
    # Cumulative probabilities
    cum_probs = np.cumsum(probabilities)
    if not np.isclose(cum_probs[-1], 1.0):
        raise ValueError("Probabilities must sum to 1")
    
    # Initialize arrays
    points = np.zeros((iterations, 2))
    x, y = 0, 0
    
    for i in range(1, iterations):
        r = random.random()
        # Determine which transformation to use
        if r < cum_probs[0]:
            idx = 0
        elif r < cum_probs[1]:
            idx = 1
        elif r < cum_probs[2]:
            idx = 2
        else:
            idx = 3
            
        a, b, c, d, e, f = coefficients[idx]
        x, y = a*x + b*y + e, c*x + d*y + f
        points[i] = [x, y]
    
    return points[:, 0], points[:, 1]

# Plot with color gradient showing progression
def plot_color_gradient(x, y, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 12))
    
    colors = range(len(x))
    scatter = ax.scatter(x, y, s=0.5, c=colors, cmap='viridis', marker='.')
    ax.set_title("Barnsley Fern with Color Gradient")
    ax.axis('off')
    return scatter


# Create growth animation
def create_animation(x, y, fig, ax):
    scatter = ax.scatter([], [], s=0.5, color='lime', marker='.')
    ax.set_title("Barnsley Fern Growth Animation")
    ax.axis('off')
    
    def init():
        scatter.set_offsets(np.empty((0, 2)))
        return (scatter,)
    
    def update(frame):
        # Show 100 points at a time for smoother animation
        display_points = min((frame+1)*100, len(x))
        scatter.set_offsets(np.column_stack((x[:display_points], y[:display_points])))
        return (scatter,)
    
    frames = len(x)//100 + 1
    return FuncAnimation(fig, update, frames=frames, init_func=init, 
                        blit=True, interval=20, repeat=False)

# 3D Fern Generation
def barnsley_fern_3d(iterations):
    x, y, z = 0, 0, 0
    x_points, y_points, z_points = [], [], []
    
    for _ in range(iterations):
        r = random.random()
        if r < 0.01:
            x, y, z = 0, 0.16 * y, 0
        elif r < 0.86:
            x, y, z = 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6, 0.1*z
        elif r < 0.93:
            x, y, z = 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6, 0.2*z + 0.2
        else:
            x, y, z = -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44, 0.2*z - 0.2
        
        x_points.append(x)
        y_points.append(y)
        z_points.append(z)
    
    return x_points, y_points, z_points

# Dark Theme Tkinter GUI
class BarnsleyFernApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Barnsley Fern Generator")
        self.root.geometry("1000x800")
        self.set_dark_theme()
        
        # Configuration variables
        self.iterations = tk.IntVar(value=50000)
        self.color_mode = tk.StringVar(value='green')
        self.animation_running = False
        self.current_animation = None
        
        # Create UI
        self.create_widgets()
        
    # Configure dark theme colors
    def set_dark_theme(self):
        self.root.configure(bg='#1e1e1e')
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        style.configure('.', background='#1e1e1e', foreground='white')
        style.configure('TFrame', background='#1e1e1e')
        style.configure('TLabel', background='#1e1e1e', foreground='white')
        style.configure('TButton', background='#333', foreground='white')
        style.configure('TScale', background='#1e1e1e')
        style.configure('TRadiobutton', background='#1e1e1e', foreground='white')
        
    # Create all GUI components
    def create_widgets(self):
        # Control Panel Frame
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        # Iterations control
        ttk.Label(control_frame, text="Iterations:").pack()
        iterations_slider = ttk.Scale(
            control_frame, from_=1000, to=100000, variable=self.iterations,
            orient=tk.HORIZONTAL)
        iterations_slider.pack(fill=tk.X)
        
        # Color mode selection
        ttk.Label(control_frame, text="Color Mode:").pack(pady=(10, 0))
        for mode in ['green', 'gradient', 'random']:
            ttk.Radiobutton(
                control_frame, text=mode.capitalize(), variable=self.color_mode,
                value=mode).pack(anchor=tk.W)
        
        # Action buttons
        ttk.Button(control_frame, text="Generate", command=self.generate_fern).pack(pady=10, fill=tk.X)
        
        ttk.Button(control_frame, text="Animate", command=self.toggle_animation).pack(pady=5, fill=tk.X)
        
        ttk.Button(control_frame, text="3D View", command=self.generate_3d).pack(pady=5, fill=tk.X)
        
        # Display Frame
        display_frame = ttk.Frame(self.root)
        display_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        
        # Matplotlib figure
        self.fig = Figure(figsize=(8, 10), dpi=100, facecolor='#1e1e1e')
        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor('#1e1e1e')
        for spine in self.ax.spines.values():
            spine.set_color('white')
        self.ax.tick_params(colors='white')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=display_frame)
        self.canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)
        
    # Generate and display the fern
    def generate_fern(self):
        if self.current_animation:
            self.current_animation.event_source.stop()
            self.animation_running = False
        
        self.ax.clear()
        x, y = barnsley_fern(self.iterations.get())
        
        if self.color_mode.get() == 'green':
            self.ax.scatter(x, y, s=0.5, color='lime', marker='.')
        elif self.color_mode.get() == 'gradient':
            plot_color_gradient(x, y, self.ax)
        else:  # random
            colors = np.random.rand(len(x))
            self.ax.scatter(x, y, s=0.5, c=colors, cmap='hsv', marker='.')
        
        self.ax.set_title("Barnsley Fern", color='white')
        self.ax.axis('off')
        self.canvas.draw()
    
    # Toggle animation on/off
    def toggle_animation(self):
        if self.animation_running:
            if self.current_animation:
                self.current_animation.event_source.stop()
            self.animation_running = False
            return
        
        self.ax.clear()
        x, y = barnsley_fern(self.iterations.get())
        self.current_animation = create_animation(x, y, self.fig, self.ax)
        self.animation_running = True
        self.canvas.draw()
    
    # Generate 3D fern in a new window
    def generate_3d(self):
        if self.current_animation:
            self.current_animation.event_source.stop()
            self.animation_running = False
        
        # Create 3D plot in new window
        x, y, z = barnsley_fern_3d(self.iterations.get())
        
        fig = plt.figure(figsize=(10, 10), facecolor='#1e1e1e')
        ax = fig.add_subplot(111, projection='3d')
        ax.set_facecolor('#1e1e1e')
        
        # Customize 3D plot colors
        ax.xaxis.set_pane_color((0.1, 0.1, 0.1, 0.0))
        ax.yaxis.set_pane_color((0.1, 0.1, 0.1, 0.0))
        ax.zaxis.set_pane_color((0.1, 0.1, 0.1, 0.0))
        ax.xaxis._axinfo["grid"]['color'] = (0.3, 0.3, 0.3, 0.3)
        ax.yaxis._axinfo["grid"]['color'] = (0.3, 0.3, 0.3, 0.3)
        ax.zaxis._axinfo["grid"]['color'] = (0.3, 0.3, 0.3, 0.3)
        ax.tick_params(colors='white')
        
        # Plot 3D fern
        ax.scatter(x, y, z, s=0.5, color='lime', marker='.')
        ax.set_title("3D Barnsley Fern", color='white')
        ax.axis('off')
        plt.show()

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = BarnsleyFernApp(root)
    root.mainloop()