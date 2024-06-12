# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation
from sklearn.cluster import DBSCAN

# Configuration for the radar
num_spheres = 7  # Number of spheres
radio_radar = 100  # Radius of the radar

# Generate random positions for the spheres
spheres = [(random.uniform(-radio_radar, radio_radar), random.uniform(-radio_radar, radio_radar)) for _ in range(num_spheres)]

# Configuration for DBSCAN
dbscan = DBSCAN(eps=15, min_samples=1)  # Set the epsilon value and minimum samples for DBSCAN
labels = dbscan.fit_predict(spheres)

# Create the figure and axes
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-radio_radar, radio_radar)
ax.set_ylim(-radio_radar, radio_radar)
ax.set_aspect('equal')  # Set the aspect ratio to ensure the radar is a circle

# Draw the circle of the radar
circle = plt.Circle((0, 0), radio_radar, color='green', fill=False)
ax.add_artist(circle)

# Create a dictionary to count the spheres in each cluster
clusters = {}
for label in set(labels):
    clusters[label] = []
    for i, pos in enumerate(spheres):
        if labels[i] == label:
            clusters[label].append(pos)

# Draw the clusters of spheres with the total number of Dragon Balls in each cluster
points = []
texts = []
for label, positions in clusters.items():
    x, y = np.mean(positions, axis=0)
    point, = ax.plot(x, y, 'yo', markersize=15)  # 'yo' indicates yellow points and large size
    text = ax.text(x, y, str(len(positions)), fontsize=12, ha='center', va='center', color='black')
    points.append(point)
    texts.append(text)

# Draw the grid lines of the radar
for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
    ax.plot([0, radio_radar * np.cos(angle)], [0, radio_radar * np.sin(angle)], color='green')

for r in np.linspace(0, radio_radar, 5):
    circle = plt.Circle((0, 0), r, color='green', fill=False, linestyle='dotted')
    ax.add_artist(circle)

# Draw an equilateral triangle at the point (0,0)
triangle = plt.Polygon([(5, 0), (-5, 0), (0, 10)], color='red', fill=True)
ax.add_artist(triangle)

# Set the titles and labels
ax.set_title('Dragon Ball Radar by David Caleb')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Create the radar line that will move
radar_line, = ax.plot([], [], color='red')

# Initialization function for the animation
def init():
    radar_line.set_data([], [])
    for point, text in zip(points, texts):
        point.set_visible(True)
        text.set_visible(True)
    return radar_line, *points, *texts

# Update function for the animation
def update(frame):
    angle = frame * np.pi / 180  # Convert the frame to an angle in radians
    x = [0, radio_radar * np.cos(angle)]
    y = [0, radio_radar * np.sin(angle)]
    radar_line.set_data(x, y)
    
    # Make the points and texts blink
    visible = frame % 20 < 10
    for point, text in zip(points, texts):
        point.set_visible(visible)
        text.set_visible(visible)
    
    return radar_line, *points, *texts

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), init_func=init, blit=True, interval=50)

# Show the radar
plt.grid(True)
plt.show()
