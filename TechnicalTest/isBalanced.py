# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Determine if the binary tree is height-balanced.
    def isBalanced(self, root) -> bool:
        """        
        root: The root node of the binary tree.
        return: True if the tree is height-balanced, False otherwise.
        """
        
        # Helper function to check the balance of the tree and 
        # return the height of the subtree rooted at 'node'.
        def check_balance(node):
            """
            node: The current node being checked.
            return: The height of the subtree if balanced, otherwise -1.
            """
            # Base case: An empty subtree is balanced and has height -1
            if not node:
                return 0
            
            # Recursively check the left subtree
            left_height = check_balance(node.left)
            if left_height == -1:  # Left subtree is not balanced
                return -1
            
            # Recursively check the right subtree
            right_height = check_balance(node.right)
            if right_height == -1:  # Right subtree is not balanced
                return -1
            
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return -1  # Current node is not balanced
            
            # Return the height of the current subtree
            return max(left_height, right_height) + 1
        
        # Start checking balance from the root
        return check_balance(root) != -1

# Helper function to build a binary tree from a list

# Convert a list to a binary tree using level-order traversal.
def build_tree_from_list(values):
    if not values:
        return None
    
    # Create the root of the tree
    root = TreeNode(values[0])
    queue = [root]
    index = 1

    while queue and index < len(values):
        node = queue.pop(0)
        
        # Add the left child
        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        
        # Ensure index is within range and add the right child
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
root1 = [3, 9, 20, None, None, 15, 7]
print("Example 1:")
print("Input root1:", root1)
tree1 = build_tree_from_list(root1)
print("Output:", sol.isBalanced(tree1))
print("=".center(50, "="))

# Example 2
root2 = [1,2,2,3,3,None,None,4,4]
print("Example 2:")
print("Input root2:", root2)
tree2 = build_tree_from_list(root2)
print("Output:", sol.isBalanced(tree2))
print("=".center(50, "="))

# Example 3
root3 = []
print("Example 3:")
print("Input root3:", root3)
tree3 = build_tree_from_list(root3)
print("Output:", sol.isBalanced(tree3))
print("=".center(50, "="))