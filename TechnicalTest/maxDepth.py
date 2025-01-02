# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  
        self.left = left
        self.right = right

class Solution:
    # Calculate the maximum depth of a binary tree.
    def maxDepth(self, root) -> int:
        """    
        root: The root node of the binary tree.
        return: The maximum depth as an integer.
        """
        # Base case: if the current node is None, return depth 0
        if root is None:
            return 0
        
        # Recursively find the depth of the left subtree
        left_depth = self.maxDepth(root.left)
        
        # Recursively find the depth of the right subtree
        right_depth = self.maxDepth(root.right)
        
        # The maximum depth is the greater of the two subtrees plus one for the current node
        return max(left_depth, right_depth) + 1

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
print("Output:", sol.maxDepth(tree1))
print("=".center(50, "="))

# Example 2
root2 = [1, None, 2]
print("Example 2:")
print("Input root2:", root2)
tree2 = build_tree_from_list(root2)
print("Output:", sol.maxDepth(tree2))
print("=".center(50, "="))
