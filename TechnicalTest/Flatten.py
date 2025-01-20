# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root) -> None:
        """
        Flatten the binary tree into a linked list in-place.
        The linked list should follow the pre-order traversal of the tree.
        """
        # Base case: if the root is None, return
        if not root:
            return
        
        # Flatten the left subtree
        if root.left:
            self.flatten(root.left)
        
        # Flatten the right subtree
        if root.right:
            self.flatten(root.right)
        
        # Store the right subtree
        temp_right = root.right
        
        # Move the left subtree to the right
        root.right = root.left
        
        # Set left child to None since we are flattening the tree
        root.left = None
        
        # Find the rightmost node of the new right subtree
        current = root
        while current.right:
            current = current.right
        
        # Attach the original right subtree to the end of the new right subtree
        current.right = temp_right

def build_tree_from_list(values):
    """Helper function to build a binary tree from a list."""
    if not values:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    
    for node in nodes:
        if node is not None:
            if kids: 
                node.left = kids.pop()
            if kids: 
                node.right = kids.pop()
    
    return root

def print_flattened_tree(root):
    """Helper function to print flattened tree as a list."""
    result = []
    while root:
        result.append(root.val)
        root = root.right
    return result

# Example usage
sol = Solution()

# Example 1
print("=".center(50, "="))
print("Example 1:")
root1 = [1, 2, 5, 3, 4, None, 6]
tree1 = build_tree_from_list(root1)
sol.flatten(tree1) 
output1 = print_flattened_tree(tree1)
print("Input:", root1)
print("Output:", output1)
print("=".center(50, "="))

# Example 2
print("Example 2:")
root2 = []
tree2 = build_tree_from_list(root2)
sol.flatten(tree2) 
output2 = print_flattened_tree(tree2)
print("Input:", root2)
print("Output:", output2)
print("=".center(50, "="))

# Example 3
print("Example 3:")
root3 = [0]
tree3 = build_tree_from_list(root3)
sol.flatten(tree3) 
output3 = print_flattened_tree(tree3)
print("Input:", root3)
print("Output:", output3)
print("=".center(50, "="))
