from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Helper function to compute the maximum gain from a node
        def max_gain(node):
            nonlocal max_sum  # Use nonlocal to modify the outer scope variable
            if not node:
                return 0
            
            # Recursively compute the maximum gain from the left and right subtrees
            left_gain = max(max_gain(node.left), 0)  # Ignore negative gains
            right_gain = max(max_gain(node.right), 0)  # Ignore negative gains
            
            # Calculate the price of the current path: node.val + left_gain + right_gain
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum sum if the current path sum is greater
            max_sum = max(max_sum, current_path_sum)
            
            # Return the maximum gain if we continue the same path
            return node.val + max(left_gain, right_gain)
        
        # Initialize max_sum with negative infinity to handle negative values
        max_sum = float('-inf')
        max_gain(root)  # Start the recursion
        return max_sum

# Helper function to create a binary tree from a list of values (for testing)
def create_tree(values, index=0):
    if index >= len(values) or values[index] is None:
        return None
    root = TreeNode(values[index])
    root.left = create_tree(values, 2 * index + 1)
    root.right = create_tree(values, 2 * index + 2)
    return root

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
values1 = [1, 2, 3]
root1 = create_tree(values1)
print("Example 1:")
print("Input tree:", values1)
print("Output:", sol.maxPathSum(root1))

# Example 2
print("=".center(50, "="))
values2 = [-10, 9, 20, None, None, 15, 7]
root2 = create_tree(values2)
print("Example 2:")
print("Input tree:", values2)
print("Output:", sol.maxPathSum(root2))
print("=".center(50, "="))