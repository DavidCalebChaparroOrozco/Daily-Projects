from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if the current node is None, return False
        if not root:
            return False
        
        # If we reach a leaf node, check if the path sum equals targetSum
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Subtract the current node's value from targetSum and check both subtrees
        targetSum -= root.val
        return (self.hasPathSum(root.left, targetSum) or 
                self.hasPathSum(root.right, targetSum))

# Function to build a binary tree from a list representation
def build_tree_from_list(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    index = 1
    
    while index < len(values):
        node = queue.pop(0)
        
        # Assign left child
        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        
        index += 1
        
        # Assign right child
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        
        index += 1
    
    return root

# Example usage
sol = Solution()

# Example 1
print("=".center(50, "="))
print("Example 1:")
root1 = [5,4,8,11,None,13,4,7,2,None,None,None,1]
tree1 = build_tree_from_list(root1)
output1 = sol.hasPathSum(tree1, 3) 
print("Input:", root1)
print("Output:", output1)
print("=".center(50, "="))

# Example 2
print("Example 2:")
root2 = [1, 2, 3]
tree2 = build_tree_from_list(root2)
output2 = sol.hasPathSum(tree2, 4) 
print("Input:", root2)
print("Output:", output2)
print("=".center(50, "="))

# Example 3
print("Example 3:")
root3 = []
tree3 = build_tree_from_list(root3)
output3 = sol.hasPathSum(tree3, 0) 
print("Input:", root3)
print("Output:", output3)
print("=".center(50, "="))