from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Initialize the result list to store all valid paths
        result = []
        
        # Helper function to perform DFS traversal
        def dfs(node, current_path, current_sum):
            # Base case: if the current node is None, return
            if not node:
                return
            
            # Add the current node's value to the path and update the sum
            current_path.append(node.val)
            current_sum += node.val
            
            # Check if we are at a leaf node and if the path sum equals targetSum
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(current_path))  # Append a copy of the current path
            
            # Continue the DFS on left and right children
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)
            
            # Backtrack: remove the last added value before returning to explore other paths
            current_path.pop()
        
        # Start DFS from the root
        dfs(root, [], 0)
        return result

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
root1 = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
tree1 = build_tree_from_list(root1)
output1 = sol.pathSum(tree1, 22)  
print("Input:", root1)
print("Output:", output1)
print("=".center(50, "="))

# Example 2
print("Example 2:")
root2 = [1, 2, 3]
tree2 = build_tree_from_list(root2)
output2 = sol.pathSum(tree2, 5)  
print("Input:", root2)
print("Output:", output2)
print("=".center(50, "="))

# Example 3
print("Example 3:")
root3 = [1, 2]
tree3 = build_tree_from_list(root3)
output3 = sol.pathSum(tree3, 0)  
print("Input:", root3)
print("Output:", output3)
print("=".center(50, "="))