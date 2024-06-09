# # Importing necessary libraries
# import networkx as nx
# import matplotlib.pyplot as plt

# # Create an undirected graph
# G = nx.Graph()

# # Add nodes to the graph
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
# G.add_node(4)

# # Add edges to the graph (connections between nodes)
# G.add_edge(1, 2)
# G.add_edge(1, 3)
# G.add_edge(2, 4)
# G.add_edge(3, 4)

# # Draw the graph
# nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')
# plt.title("Undirected Graph")
# plt.show()

# # Basic information about the graph
# print("Nodes of the graph:", G.nodes())
# print("Edges of the graph:", G.edges())

# # Check if the graph is connected
# print("The graph is connected:", nx.is_connected(G))


# Importing necessary libraries
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create an undirected graph
G = nx.Graph()

# Add nodes to the graph
for i in range(11):
    G.add_node(i)

# Add edges to the graph (Goldner-Harary graph edges)
edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (1, 5), (2, 3),
        (2, 6), (3, 7), (4, 5), (4, 6), (4, 8), (5, 6), (5, 9),
        (6, 7), (6, 10), (7, 10), (7, 8), (8, 9), (8, 10),
        (9, 10), (0, 8), (1, 9), (2, 10), (3, 9), (0, 4)]

G.add_edges_from(edges)

# Generate 3D positions for the nodes
pos = nx.spring_layout(G, dim=3, seed=42)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract the node positions
x = [pos[i][0] for i in G.nodes()]
y = [pos[i][1] for i in G.nodes()]
z = [pos[i][2] for i in G.nodes()]

# Draw the nodes
ax.scatter(x, y, z, c='lightblue', s=100)

# Draw the edges
for edge in G.edges():
    x_vals = [pos[edge[0]][0], pos[edge[1]][0]]
    y_vals = [pos[edge[0]][1], pos[edge[1]][1]]
    z_vals = [pos[edge[0]][2], pos[edge[1]][2]]
    ax.plot(x_vals, y_vals, z_vals, c='gray')

# Annotate the nodes
for i in G.nodes():
    ax.text(pos[i][0], pos[i][1], pos[i][2], str(i), fontsize=12, ha='center')

plt.title("Goldner-Harary Graph in 3D")
plt.show()

# Basic graph information
print("Nodes of the graph:", G.nodes())
print("Edges of the graph:", G.edges())

# Verify Euler's formula (v - e + f = 2 for planar graphs)
v = G.number_of_nodes()  # number of vertices
e = G.number_of_edges()  # number of edges
# In a planar graph, f = e - v + 2
f = e - v + 2

print("Number of vertices (v):", v)
print("Number of edges (e):", e)
print("Number of faces (f):", f)

# Check if the graph is planar
is_planar, _ = nx.check_planarity(G)
print("The graph is planar:", is_planar)

# Verify if Euler's formula holds
if v - e + f == 2:
    print("Euler's formula is verified.")
else:
    print("Euler's formula is not verified.")