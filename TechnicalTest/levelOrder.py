from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  
        self.left = left 
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize an empty list to hold the result
        result = []
        
        # If the tree is empty, return an empty list
        if not root:
            return result
        
        # Use a queue to facilitate level order traversal
        queue = deque([root])
        
        # Loop until there are no more nodes to process
        while queue:
            # Get the number of nodes at the current level
            level_size = len(queue)
            # Initialize a list to hold the values of nodes at this level
            current_level = []
            
            # Process all nodes at the current level
            for _ in range(level_size):
                # Remove the front node from the queue
                node = queue.popleft()
                # Add its value to the current level list
                current_level.append(node.val)
                
                # Add the left child to the queue if it exists
                if node.left:
                    queue.append(node.left)
                # Add the right child to the queue if it exists
                if node.right:
                    queue.append(node.right)
            
            # Add the current level's values to the result list
            result.append(current_level)
        
        # Return the final result containing level order traversal
        return result  

# Helper function to build a binary tree from a list.
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = deque([root])
    index = 1
    
    while index < len(nodes):
        node = queue.popleft()
        
        if nodes[index] is not None:
            node.left = TreeNode(nodes[index])
            queue.append(node.left)
        
        index += 1
        
        if index < len(nodes) and nodes[index] is not None:
            node.right = TreeNode(nodes[index])
            queue.append(node.right)
        
        index += 1
    
    return root

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
root1 = [3,9,20,None,None,15,7]
print("Example 1:")
print("Input:", root1)
tree1 = build_tree(root1)  
print("Output:", sol.levelOrder(tree1))
print("=".center(50,"="))

# Example 2
root2 = [1]
print("Example 2:")
print("Input:", root2)
tree2 = build_tree(root2)  
print("Output:", sol.levelOrder(tree2))
print("=".center(50,"="))

# Example 3
root3 = []
print("Example 3:")
print("Input:", root3)
tree3 = build_tree(root3)  
print("Output:", sol.levelOrder(tree3))
print("=".center(50,"="))
