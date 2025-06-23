# Import necessary libraries
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc, RegularPolygon
import numpy as np

class BasketballDefenseVisualizer:
    # Initialize the basketball defense visualizer with a specific formation.
    def __init__(self, formation='2-3'):
        """    
        Args:
            formation: Defensive formation type ('2-3' or '3-2')
        """

        self.formation = formation
        # Initial ball position
        self.ball_position = [25, 10]  
        # Dictionary to store defensive coverage areas
        self.coverage_zones = {}  
        # Track which player is being dragged
        self.selected_player = None  

        # Court dimensions (half court)
        self.court_width = 50
        self.court_height = 47

        # Offensive team positions (circles) and defensive team positions (triangles)
        self.attackers = [[10, 30], [25, 35], [40, 30], [15, 20], [35, 20]]
        # Initialize defenders based on formation
        self.setup_defenders()  

        # Create figure and set up event handlers for interactivity
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_drag)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)

        # Draw initial visualization
        self.visualize()

    # Initialize defender positions based on the selected formation.
    def setup_defenders(self):
        if self.formation == '2-3':
            # 2-3 zone defense positions (two up top, three near the basket)
            self.defenders = [[15, 15], [35, 15], [10, 5], [25, 5], [40, 5]]
        elif self.formation == '3-2':
            # 3-2 zone defense positions (three up top, two near the basket)
            self.defenders = [[10, 20], [25, 20], [40, 20], [17, 5], [33, 5]]

    # Draw the basketball court with all markings.
    def draw_court(self):
        # Set background color (orange)
        self.ax.set_facecolor('#eb8c34')
        
        # Main court rectangle (blue)
        self.ax.add_patch(Rectangle((0, 0), 50, 47, linewidth=2, edgecolor='white', facecolor='#0080FF'))

        # Three-point arc
        self.ax.add_patch(Arc((25, 5), 40, 40, theta1=0, theta2=180, color='white', lw=2))
        self.ax.plot([5, 5], [0, 5], 'white', lw=2)  # Left corner line
        self.ax.plot([45, 45], [0, 5], 'white', lw=2)  # Right corner line

        # Key/paint area
        self.ax.add_patch(Rectangle((17, 0), 16, 19, linewidth=2, edgecolor='white', fill=False))

        # Free throw circle
        self.ax.add_patch(Arc((25, 19), 12, 12, theta1=0, theta2=360, color='white', lw=2))

        # Basket and rim

        # Backboard
        self.ax.add_patch(Circle((25, 5), 0.75, color='#ed2d05'))  
        # Rim
        self.ax.add_patch(Circle((25, 5), 1.5, edgecolor='white', fill=False, lw=2))  

        # Center circle (top of the court)
        self.ax.add_patch(Circle((25, 47), 6, edgecolor='white', fill=False, lw=2))

    # Update the entire visualization.
    def visualize(self):
        self.ax.clear()
        # Draw court markings
        self.draw_court()  
        # Draw all players
        self.draw_players()  
        # Draw defensive coverage zones
        self.draw_coverage()  

        # Set plot properties
        self.ax.set_xlim(0, self.court_width)
        self.ax.set_ylim(0, self.court_height)
        self.ax.set_aspect('equal')
        self.ax.set_title(f"{self.formation} Zone Defense (Interactive) by David Caleb")
        # Hide axes
        self.ax.axis('off')  
        # Update the figure
        self.fig.canvas.draw()  

    # Draw all players (defenders, attackers) and the ball.
    def draw_players(self):
        self.artists = {'defenders': [], 'attackers': [], 'ball': None}
        
        # Draw defenders as triangles with numbers
        for i, (x, y) in enumerate(self.defenders):
            tri = RegularPolygon((x, y), numVertices=3, radius=1.5, orientation=np.pi, color='lightcoral', ec='black')
            self.ax.add_patch(tri)
            self.ax.text(x, y, str(i + 1), color='black', ha='center', va='center')
            self.artists['defenders'].append(tri)

        # Draw attackers as circles with numbers
        for i, (x, y) in enumerate(self.attackers):
            circ = Circle((x, y), 1.5, color='lightblue', ec='black')
            self.ax.add_patch(circ)
            self.ax.text(x, y, str(i + 1), color='black', ha='center', va='center')
            self.artists['attackers'].append(circ)

        # Draw the ball as a black circle
        self.artists['ball'] = self.ax.plot(
            self.ball_position[0], self.ball_position[1], 
            'ko', markersize=10)[0]

    # Draw the defensive coverage zones.
    def draw_coverage(self):
        # Recalculate coverage areas
        self.calculate_coverage()  
        
        # Draw each coverage zone as a semi-transparent rectangle
        for pos, did in self.coverage_zones.items():
            self.ax.add_patch(Rectangle(
                (pos[0] - 1.5, pos[1] - 1.5), 3, 3,
                color='lightcoral', alpha=0.2))

    # Calculate which areas each defender should cover.
    def calculate_coverage(self):
        self.coverage_zones = {}
        
        # For each defender, recursively expand their coverage area
        for i, pos in enumerate(self.defenders):
            self.expand_zone(i + 1, pos, 0)

    # Recursively expand a defender's coverage zone.
    def expand_zone(self, did, pos, depth):
        """  
        Args:
            did: Defender ID
            pos: Current (x,y) position to evaluate
            depth: Recursion depth (to limit expansion)
        """
        # Base case: stop if recursion too deep
        if depth > 3: 
            return
            
        x, y = pos
        # Check if position is within court bounds
        if not (0 <= x <= self.court_width and 0 <= y <= self.court_height):
            return
            
        # Use rounded coordinates as dictionary keys
        rounded = (round(x), round(y))
        if rounded in self.coverage_zones: 
            return
            
        # If this defender is best for this position, claim it
        if self.is_best_defender(did, pos):
            self.coverage_zones[rounded] = did
            # Recursively check adjacent positions
            for dx, dy in [(-3, 0), (3, 0), (0, -3), (0, 3)]:
                self.expand_zone(did, (x + dx, y + dy), depth + 1)

    # Determine if a defender is the best candidate to cover a position.
    def is_best_defender(self, did, pos):
        """        
        Args:
            did: Defender ID to check
            pos: (x,y) position to evaluate
            
        Returns:
            bool: True if this defender should cover this position
        """
        # Calculate distance from this defender to the position
        my_dist = np.linalg.norm(np.array(self.defenders[did - 1]) - np.array(pos))
        
        # Calculate distance from ball to the position
        ball_dist = np.linalg.norm(np.array(self.ball_position) - np.array(pos))
        
        # Calculate distances from other defenders to the position
        other_dists = [
            np.linalg.norm(np.array(dpos) - np.array(pos))
            for i, dpos in enumerate(self.defenders) if (i + 1) != did
]
        
        # This defender is best if:
        # 1. Closer than other defenders, and
        # 2. Position is reasonably close to the ball
        return (my_dist < min(other_dists, default=99) and ball_dist < 20)

    # Handle mouse click events to select players.
    def on_click(self, event):
        if not event.inaxes: 
            return
            
        x, y = event.xdata, event.ydata
        
        # Check if ball was clicked
        if np.hypot(x - self.ball_position[0], y - self.ball_position[1]) < 2:
            self.selected_player = ('ball', 0)
            return
            
        # Check if any defender was clicked
        for i, (dx, dy) in enumerate(self.defenders):
            if np.hypot(x - dx, y - dy) < 2:
                self.selected_player = ('defender', i)
                return
                
        # Check if any attacker was clicked
        for i, (ax, ay) in enumerate(self.attackers):
            if np.hypot(x - ax, y - ay) < 2:
                self.selected_player = ('attacker', i)
                return

    # Handle mouse drag events to move players.
    def on_drag(self, event):
        if not self.selected_player or not event.inaxes: 
            return
            
        x, y = event.xdata, event.ydata
        role, idx = self.selected_player
        
        # Move the selected item
        if role == 'ball':
            self.ball_position = [x, y]
        elif role == 'defender':
            self.defenders[idx] = [x, y]
        elif role == 'attacker':
            self.attackers[idx] = [x, y]
            
        # Redraw the visualization
        self.visualize()

    # Handle mouse release events to stop dragging.
    def on_release(self, event):
        self.selected_player = None

if __name__ == "__main__":
    # Create and display the visualization
    vis = BasketballDefenseVisualizer(formation='2-3')
    plt.show()

# Quote:
# "If you get tired, learn to rest, not to quit." ~Banksy