# Importing necessary libraries
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

# Node of a binary tree with enhanced features
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.x = 0  # x-coordinate for visualization
        self.y = 0  # y-coordinate for visualization

# Inverts a binary tree (creates its mirror image) recursively
def mirror_tree(root):
    """

    Example:
        Original:      1     Mirrored:    1
                      / \                / \
                     2   3              3   2
    """
    if root is None:
        return None
    
    # Swap the left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively mirror both subtrees
    mirror_tree(root.left)
    mirror_tree(root.right)
    
    return root

# Builds a binary tree from a list representation (level-order/BFS)
def build_tree_from_list(tree_list):
    """
    Example: [1, 2, 3, 4, 5] 
    creates:
            1
           / \
          2   3
         / \
        4   5
    """
    if not tree_list:
        return None
    
    root = TreeNode(tree_list[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(tree_list):
        current = queue.popleft()
        
        # Left child
        if i < len(tree_list) and tree_list[i] is not None:
            current.left = TreeNode(tree_list[i])
            queue.append(current.left)
        i += 1
        
        # Right child
        if i < len(tree_list) and tree_list[i] is not None:
            current.right = TreeNode(tree_list[i])
            queue.append(current.right)
        i += 1
    
    return root

# Creates a visual representation of the binary tree using matplotlib
def visualize_binary_tree(root, title="Binary Tree"):
    if not root:
        print("Empty tree cannot be visualized")
        return
    
    # Create a directed graph
    G = nx.DiGraph()
    positions = {}
    labels = {}
    
    # BFS to assign positions and build the graph
    queue = deque([(root, 0, 0)])
    max_depth = 0
    
    while queue:
        node, x, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        positions[node] = (x, -depth)
        labels[node] = str(node.val)
        
        if node.left:
            G.add_edge(node, node.left)
            # Calculate position for left child
            queue.append((node.left, x - 2**(max_depth - depth), depth + 1))
        
        if node.right:
            G.add_edge(node, node.right)
            # Calculate position for right child
            queue.append((node.right, x + 2**(max_depth - depth), depth + 1))
    
    # Adjust x-coordinates to prevent overlap
    scale = 1.5
    pos = {node: (x * scale, y) for node, (x, y) in positions.items()}
    
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=1000,
            node_color='lightblue', font_size=12, font_weight='bold',
            arrows=False)
    plt.title(title, fontsize=14)
    plt.axis('off')
    plt.show()

# Prints the tree using specified traversal method with clear formatting
def print_tree_info(root, traversal_type='inorder'):
    def helper(node):
        if node:
            if traversal_type == 'preorder':
                print(node.val, end=' ')
                helper(node.left)
                helper(node.right)
            elif traversal_type == 'inorder':
                helper(node.left)
                print(node.val, end=' ')
                helper(node.right)
            elif traversal_type == 'postorder':
                helper(node.left)
                helper(node.right)
                print(node.val, end=' ')
    
    print(f"\n{traversal_type.capitalize()} traversal: [", end='')
    helper(root)
    print("]")

# Interactive demonstration of the mirror tree functionality
def interactive_demo():
    print("\n" + "="*50)
    print("Binary Tree Mirror - Interactive Demo")
    print("="*50)
    
    # Get tree input from user
    print("\nEnter tree values in level-order (BFS) order.")
    print("Use space-separated numbers and 'None' for empty nodes")
    print("Example: 1 2 3 None 5 (creates: 1 / 2 3 / None 5)")
    
    while True:
        try:
            user_input = input("\nEnter tree values: ").strip()
            values = []
            for item in user_input.split():
                if item.lower() == 'none':
                    values.append(None)
                else:
                    values.append(int(item))
            
            original_tree = build_tree_from_list(values)
            print("\nOriginal Tree:")
            visualize_binary_tree(original_tree, "Original Tree")
            
            print("\nTree Information:")
            print_tree_info(original_tree, 'preorder')
            print_tree_info(original_tree, 'inorder')
            print_tree_info(original_tree, 'postorder')
            
            input("\nPress Enter to mirror the tree...")
            
            mirrored_tree = mirror_tree(original_tree)
            print("\nMirrored Tree:")
            visualize_binary_tree(mirrored_tree, "Mirrored Tree")
            
            print("\nMirrored Tree Information:")
            print_tree_info(mirrored_tree, 'preorder')
            print_tree_info(mirrored_tree, 'inorder')
            print_tree_info(mirrored_tree, 'postorder')
            
            choice = input("\nTry another tree? (y/n): ").lower()
            if choice != 'y':
                print("\nDemo complete. Goodbye!")
                break
                
        except ValueError:
            print("Invalid input. Please enter numbers or 'None'.")

if __name__ == "__main__":
    # Example with automatic demonstration
    print("Automatic Demonstration with Sample Tree")
    print("="*50)
    
    # Sample tree
    sample_tree = build_tree_from_list([1, 2, 3, 4, 5, None, 6, None, None, 7])
    
    print("\nOriginal Sample Tree:")
    visualize_binary_tree(sample_tree, "Original Sample Tree")
    
    print("\nOriginal Tree Information:")
    print_tree_info(sample_tree, 'preorder')
    print_tree_info(sample_tree, 'inorder')
    print_tree_info(sample_tree, 'postorder')
    
    # Mirror the tree
    mirrored_sample = mirror_tree(sample_tree)
    
    print("\nMirrored Sample Tree:")
    visualize_binary_tree(mirrored_sample, "Mirrored Sample Tree")
    
    print("\nMirrored Tree Information:")
    print_tree_info(mirrored_sample, 'preorder')
    print_tree_info(mirrored_sample, 'inorder')
    print_tree_info(mirrored_sample, 'postorder')
    
    # Start interactive demo
    interactive_demo()