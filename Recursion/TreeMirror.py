# Import necessary libraries
import matplotlib.pyplot as plt
import networkx as nx

# Define the structure of a binary tree node
class TreeNode:
    def __init__(self, value):
        # Value of the node
        self.value = value  
        # Left child
        self.left = None    
        # Right child
        self.right = None   

# Function to create a mirror of a binary tree using recursion
def mirror_tree(node):
    if node is None:
        return None
    
    # Swap the left and right children
    node.left, node.right = node.right, node.left
    
    # Recursively mirror the left and right subtrees
    mirror_tree(node.left)
    mirror_tree(node.right)
    
    return node

# Function to visualize the binary tree using NetworkX and Matplotlib
def visualize_tree(node, graph=None, pos=None, x=0, y=0, layer=1):
    if graph is None:
        graph = nx.Graph()
    if pos is None:
        pos = {}
    
    if node is not None:
        # Add the current node to the graph
        graph.add_node(node.value)
        pos[node.value] = (x, y)
        
        # Recursively add left and right children
        if node.left is not None:
            graph.add_edge(node.value, node.left.value)
            visualize_tree(node.left, graph, pos, x - 1 / layer, y - 1, layer + 1)
        if node.right is not None:
            graph.add_edge(node.value, node.right.value)
            visualize_tree(node.right, graph, pos, x + 1 / layer, y - 1, layer + 1)
    
    return graph, pos

# Function to plot the binary tree
def plot_tree(tree, title):
    graph, pos = visualize_tree(tree)
    plt.figure(figsize=(8, 6))
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=12, font_weight="bold")
    plt.title(title)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Visualize the original tree
    print("Original Tree:")
    plot_tree(root, "Original Binary Tree")

    # Create the mirror of the tree
    mirrored_root = mirror_tree(root)

    # Visualize the mirrored tree
    print("Mirrored Tree:")
    plot_tree(mirrored_root, "Mirrored Binary Tree")