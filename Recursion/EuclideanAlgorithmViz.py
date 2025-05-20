# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.widgets import Button

# A class to visualize the Euclidean algorithm for finding GCD of two numbers.
# The visualization shows the division steps geometrically with colored rectangles.
class EuclideanAlgorithmViz:
    
    # Initialize with two positive integers a and b.
    def __init__(self, a, b):
        """    
        Args:
            a: First positive integer
            b: Second positive integer
        """
        self.original_a = a
        self.original_b = b
        self.a = max(a, b)  # Ensure a is the larger number
        self.b = min(a, b)  # Ensure b is the smaller number
        self.steps = []     # Store algorithm steps
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.current_step = -1     # Start before first step (-1 = initial state)
        self.colors = plt.cm.tab20.colors  # Color palette for rectangles
        self.gcd = None     # Will store the final GCD
        
    # Recursive Euclidean algorithm that records each division step.
    def compute_gcd(self, a, b):
        """    
        Args:
            a: Current larger number
            b: Current smaller number
            
        Returns:
            int: GCD of a and b
        """
        if b == 0:
            return a
        quotient = a // b
        remainder = a % b
        # Record this division step
        self.steps.append({
            'a': a,
            'b': b,
            'quotient': quotient,
            'remainder': remainder,
            'operation': f"{a} = {quotient} × {b} + {remainder}"
        })
        return self.compute_gcd(b, remainder)
    
    # Compute GCD and launch interactive visualization.
    def visualize_algorithm(self):
        # Apply seaborn styling
        sns.set_theme(style="whitegrid")
        
        # Compute steps and GCD
        self.gcd = self.compute_gcd(self.a, self.b)
        
        # Setup the visualization
        self._setup_figure()
        self._draw_initial()
        self._add_navigation_buttons()
        
        plt.tight_layout()
        plt.show()
    
    # Configure figure title and basic properties.
    def _setup_figure(self):
        self.fig.suptitle(
            f"Euclidean Algorithm Visualization\nFinding GCD of {self.original_a} and {self.original_b}",
            fontsize=14
        )
        self.ax.set_xlabel('Length')
        self.ax.set_ylabel('Width')
        self.ax.set_aspect('equal')
        self.ax.grid(True, linestyle='--', alpha=0.7)
        
        # Add decorative spiral in the background
        theta = np.linspace(0, 4 * np.pi, 1000)
        r = (self.a / 2) * theta / (theta.max())
        x = r * np.cos(theta) + self.a / 2
        y = r * np.sin(theta) + self.b / 2
        self.ax.plot(x, y, linewidth=0.5, alpha=0.3)
    
    # Draw the initial rectangle representing a × b
    def _draw_initial(self):
        self.current_step = -1
        self.ax.clear()
        self._setup_figure()
        
        # Draw main rectangle
        rect = Rectangle((0, 0), self.a, self.b,
                        facecolor=self.colors[0],
                        edgecolor='black',
                        label=f'{self.a} × {self.b}')
        self.ax.add_patch(rect)
        
        # Set appropriate axis limits
        max_dim = max(self.a, self.b) * 1.2
        self.ax.set_xlim(0, max_dim)
        self.ax.set_ylim(0, max_dim)
        
        # Add legend and step information
        self.ax.legend(loc='upper right')
        self.ax.text(0.02, 0.98, "Step 0: Initial rectangle",
                    transform=self.ax.transAxes, va='top')
        
        plt.draw()
    
    # Draw a specific step of the algorithm.
    def _draw_step(self, idx):
        """
        Args:
            idx: Index of the step to draw (0-based)
        """
        if idx < 0 or idx >= len(self.steps):
            return
            
        self.current_step = idx
        step = self.steps[idx]
        a, b = step['a'], step['b']
        q, r = step['quotient'], step['remainder']
        
        self.ax.clear()
        self._setup_figure()
        
        # Draw the main rectangle
        self.ax.add_patch(Rectangle((0, 0), a, b,
                            facecolor=self.colors[0],
                            edgecolor='black'))
        
        # Draw q squares of size b×b
        for i in range(q):
            self.ax.add_patch(Rectangle((i * b, 0), b, b,
                                facecolor=self.colors[(i+1) % len(self.colors)],
                                edgecolor='black',
                                alpha=0.7))
            self.ax.text(i * b + b/2, b/2, f'{b}×{b}',
                        ha='center', va='center',
                        fontsize=10)
        
        # Draw remainder rectangle if it exists
        if r > 0:
            self.ax.add_patch(Rectangle((q * b, 0), r, b,
                                facecolor=self.colors[(q+2) % len(self.colors)],
                                edgecolor='black',
                                hatch='//',
                                alpha=0.7))
            self.ax.text(q * b + r/2, b/2, f'{r}×{b}',
                        ha='center', va='center',
                        fontsize=10)
        
        # Set axis limits
        max_dim = max(a, b) * 1.2
        self.ax.set_xlim(0, max_dim)
        self.ax.set_ylim(0, max_dim)
        
        # Add step information
        self.ax.text(0.02, 0.98, f"Step {idx+1}: {step['operation']}",
                    transform=self.ax.transAxes, va='top')
        
        # If this is the last step (remainder is 0), show GCD
        if r == 0:
            self.ax.text(0.02, 0.92, f"GCD found: {b}",
                        transform=self.ax.transAxes, va='top',
                        fontweight='bold', color='red')
        
        plt.draw()
    
    # Add interactive buttons for navigation between steps.
    def _add_navigation_buttons(self):
        ax_prev = plt.axes([0.2, 0.02, 0.1, 0.05])
        ax_next = plt.axes([0.5, 0.02, 0.1, 0.05])
        ax_reset = plt.axes([0.7, 0.02, 0.1, 0.05])
        
        btn_prev = Button(ax_prev, 'Previous')
        btn_next = Button(ax_next, 'Next')
        btn_reset = Button(ax_reset, 'Reset')
        
        def on_next(event):
            if self.current_step < len(self.steps) - 1:
                self._draw_step(self.current_step + 1)
            elif self.current_step == len(self.steps) - 1:
                # Already at last step
                pass
        
        def on_prev(event):
            if self.current_step > 0:
                self._draw_step(self.current_step - 1)
            elif self.current_step == 0:
                self._draw_initial()
        
        def on_reset(event):
            self._draw_initial()
        
        btn_next.on_clicked(on_next)
        btn_prev.on_clicked(on_prev)
        btn_reset.on_clicked(on_reset)

# Main entry point
if __name__ == '__main__':
    print("Euclidean Algorithm Visualization by David Caleb")
    while True:
        try:
            a = int(input("Enter first positive integer: "))
            b = int(input("Enter second positive integer: "))
            if a > 0 and b > 0:
                break
            print("Only positive integers allowed.")
        except ValueError:
            print("Invalid input. Enter integers only.")
    
    viz = EuclideanAlgorithmViz(a, b)
    viz.visualize_algorithm()