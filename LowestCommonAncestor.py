# Import necessary libraries
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

# Represents a node in a Binary Search Tree (BST).
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Handles visualization of Binary Search Trees using matplotlib.
class BSTVisualizer:
    # Visualizes the BST with optional node highlighting.
    @staticmethod
    def visualize_tree(root, highlight_nodes=None, title="Binary Search Tree by David Caleb"):
        if root is None:
            print("Tree is empty!")
            return

        if highlight_nodes is None:
            highlight_nodes = []

        # Create a directed graph
        graph = nx.DiGraph()
        pos = {}
        q = deque([(root, 0, 0)])
        
        # BFS to build the tree structure and positions
        while q:
            node, x, y = q.popleft()
            graph.add_node(node.val)
            # Invert y for top-down visualization
            pos[node.val] = (x, -y)  
            
            if node.left:
                graph.add_edge(node.val, node.left.val)
                q.append((node.left, x - 1/(y+2), y + 1))
            if node.right:
                graph.add_edge(node.val, node.right.val)
                q.append((node.right, x + 1/(y+2), y + 1))

        # Determine node colors based on highlighting
        node_colors = []
        for node in graph.nodes():
            if node in highlight_nodes:
                node_colors.append('red')
            else:
                node_colors.append('skyblue')

        plt.figure(figsize=(10, 6))
        nx.draw(graph, pos, with_labels=True, node_size=1500, node_color=node_colors, 
                font_size=10, font_weight='bold', arrows=False)
        plt.title(title)
        plt.show()

# Contains operations for Binary Search Trees including LCA finding.
class BSTOperations:
    # Finds the Lowest Common Ancestor of two nodes in a BST.
    @staticmethod
    def find_lca(root, p, q):
        current = root
        while current:
            if p.val > current.val and q.val > current.val:
                current = current.right
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                return current
        return None

    # Finds a node with the given value in the BST.
    @staticmethod
    def find_node(root, val):
        current = root
        while current:
            if val == current.val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return None

    # Builds and returns a sample BST for demonstration.
    @staticmethod
    def build_sample_bst():
        """    
        The BST structure:
              6
             / \
            2   8
           / \ / \
          0  4 7 9
            / \
           3   5
        """
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        return root

# Demonstrates the LCA functionality with visualization.
class LCADemo:
    def __init__(self):
        self.bst = BSTOperations.build_sample_bst()
        
    # Runs the interactive LCA demonstration.
    def run_demo(self):
        print("Binary Search Tree LCA Finder")
        print("Sample BST created with values: [6, 2, 8, 0, 4, 7, 9, 3, 5]")
        
        # Initial visualization
        BSTVisualizer.visualize_tree(self.bst, title="Initial BST Structure")
        
        while True:
            print("\nEnter two node values to find their LCA (or 'q' to quit):")
            val1 = input("First node value: ")
            if val1.lower() == 'q':
                break
                
            val2 = input("Second node value: ")
            if val2.lower() == 'q':
                break
                
            try:
                val1 = int(val1)
                val2 = int(val2)
                
                node1 = BSTOperations.find_node(self.bst, val1)
                node2 = BSTOperations.find_node(self.bst, val2)
                
                if node1 and node2:
                    lca = BSTOperations.find_lca(self.bst, node1, node2)
                    print(f"\nLCA of {val1} and {val2} is: {lca.val}")
                    
                    # Visualize with highlighted nodes
                    BSTVisualizer.visualize_tree(
                        self.bst, 
                        highlight_nodes=[val1, val2, lca.val],
                        title=f"LCA of {val1} and {val2} is {lca.val}"
                    )
                else:
                    missing = []
                    if not node1:
                        missing.append(str(val1))
                    if not node2:
                        missing.append(str(val2))
                    print(f"Node(s) not found in BST: {', '.join(missing)}")
                    
            except ValueError:
                print("Please enter valid integers or 'q' to quit.")

if __name__ == "__main__":
    demo = LCADemo()
    demo.run_demo()