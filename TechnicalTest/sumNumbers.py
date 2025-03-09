# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root) -> int:
        # Helper function to perform DFS traversal
        def dfs(node, current_sum):
            if not node:
                return 0  # Base case: if the node is None, return 0
            
            # Update the current sum by appending the current node's value
            current_sum = current_sum * 10 + node.val
            
            # If the node is a leaf, return the current sum
            if not node.left and not node.right:
                return current_sum
            
            # Recursively calculate the sum for the left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        # Start DFS from the root with an initial sum of 0
        return dfs(root, 0)
    
# Example usage:
sol = Solution()

# Example 1
print("=".center(50, "="))
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
print("Example 1:")
print("Input:")
print("   1")
print("  / \\")
print(" 2   3")
print("Output:", sol.sumNumbers(root1))

# Example 2
print("=".center(50, "="))
root2 = TreeNode(4)
root2.left = TreeNode(9)
root2.right = TreeNode(0)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(1)
print("Example 2:")
print("Input:")
print("    4")
print("   / \\")
print("  9   0")
print(" / \\")
print("5   1")
print("Output:", sol.sumNumbers(root2))
print("=".center(50, "="))