# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Find the minimum depth of the binary tree.
    def minDepth(self, root) -> int:
        """
        root: The root node of the binary tree.
        return: The minimum depth of the tree.
        """
        
        # Base case: If the tree is empty, the minimum depth is 0
        if not root:
            return 0
        
        # If the left subtree is None, recurse on the right subtree
        if not root.left:
            return self.minDepth(root.right) + 1
        
        # If the right subtree is None, recurse on the left subtree
        if not root.right:
            return self.minDepth(root.left) + 1
        
        # If both subtrees are present, find the minimum depth of both
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        # Return the minimum of both depths plus one for the current node
        return min(left_depth, right_depth) + 1

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
print("Output:", sol.minDepth(tree1))
print("=".center(50, "="))

# Example 2
root2 = [2,None,3,None,4,None,5,None,6]
print("Example 2:")
print("Input root2:", root2)
tree2 = build_tree_from_list(root2)
print("Output:", sol.minDepth(tree2))
print("=".center(50, "="))