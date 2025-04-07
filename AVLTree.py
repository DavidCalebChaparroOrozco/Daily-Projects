# Import necessary libraries
import matplotlib.pyplot as plt
import networkx as nx

class AVLNode:
    def __init__(self, key):
        # Node value
        self.key = key      
        # Left child
        self.left = None     
        # Right child
        self.right = None    
        # Height of the node (leaf nodes have height 1)
        self.height = 1      


# Insert a key into the AVL tree and balance it if necessary
class AVLTree:
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            # Duplicate keys not allowed
            return root  

        # Update height of current node
        root.height = 1 + max(self.get_height(root.left),
                                self.get_height(root.right))

        # Check balance factor
        balance = self.get_balance(root)

        # Perform rotations if tree becomes unbalanced
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Left rotation to balance the tree
    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                        self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                        self.get_height(y.right))
        # New root
        return y  

    # Right rotation to balance the tree
    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                        self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                        self.get_height(y.right))
        # New root
        return y  

    # Get height of a node (0 for None)
    def get_height(self, node):
        return 0 if not node else node.height

    # Get balance factor of a node (difference between left and right subtree heights)
    def get_balance(self, node):
        return 0 if not node else self.get_height(node.left) - self.get_height(node.right)

    # Pre-order traversal of the tree (root -> left -> right)
    def pre_order(self, root):
        if not root:
            return
        print(f"{root.key} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)


# Visualization class using matplotlib
class AVLVisualizer:
    def __init__(self):
        self.graph = nx.DiGraph()  # Directed graph to represent tree structure

    # Recursively build the graph representation of the tree
    def build_graph(self, node, pos=None, x=0, y=0, layer=1):
        if node is None:
            return

        # Add current node with its position
        self.graph.add_node(node.key, pos=(x, y))

        # Process left child
        if node.left:
            self.graph.add_edge(node.key, node.left.key)
            self.build_graph(node.left, pos, x - 1 / layer, y - 1, layer + 1)

        # Process right child
        if node.right:
            self.graph.add_edge(node.key, node.right.key)
            self.build_graph(node.right, pos, x + 1 / layer, y - 1, layer + 1)

    # Draw the tree using matplotlib
    def draw(self):
        pos = nx.get_node_attributes(self.graph, 'pos')
        labels = {node: node for node in self.graph.nodes()}
        plt.figure(figsize=(10, 6))
        nx.draw(self.graph, pos, with_labels=True, labels=labels,
                node_size=2000, node_color='skyblue', font_size=12,
                font_weight='bold', arrows=False)
        plt.title("AVL Tree Structure", fontsize=14)
        plt.axis('off')
        plt.show()


# Example usage
if __name__ == "__main__":
    avl = AVLTree()
    root = None

    # Nodes to insert
    elements = [20, 4, 15, 70, 50, 100, 80]

    # Build the AVL tree
    for el in elements:
        root = avl.insert(root, el)

    print("Pre-order traversal of the AVL tree:")
    avl.pre_order(root)

    # Visualize the AVL tree
    visualizer = AVLVisualizer()
    visualizer.build_graph(root)
    visualizer.draw()