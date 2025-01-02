from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)  # Convert preorder list to deque for efficient pop from the left

        def build(preorder, inorder):
            if inorder:
                idx = inorder.index(preorder.popleft())
                root = TreeNode(inorder[idx])

                # Recursively build the left and right subtrees
                root.left = build(preorder, inorder[:idx])
                root.right = build(preorder, inorder[idx+1:])

                return root

        return build(preorder, inorder)

# Helper function to convert a tree to a level-order list
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values for a cleaner representation
    while result and result[-1] is None:
        result.pop()

    return result

# Testing the implementation
sol = Solution()

# Example 1
print("=".center(50, "="))
preorder1 = [3, 9, 20, 15, 7]
inorder1 = [9, 3, 15, 20, 7]
print("Example 1:")
print("Preorder:", preorder1)
print("Inorder:", inorder1)
tree1 = sol.buildTree(preorder1, inorder1)
print("Tree as list:", tree_to_list(tree1))
print("=".center(50, "="))

# Example 2
preorder2 = [-1]
inorder2 = [-1]
print("Example 2:")
print("Preorder:", preorder2)
print("Inorder:", inorder2)
tree2 = sol.buildTree(preorder2, inorder2)
print("Tree as list:", tree_to_list(tree2))
print("=".center(50, "="))