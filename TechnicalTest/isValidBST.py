# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        # Helper function to validate the BST properties
        def validate(node, low=float('-inf'), high=float('inf')):
            # Base case: an empty node is valid
            if not node:
                return True
            
            # Current node's value must be within the valid range
            if not (low < node.val < high):
                return False
            
            # Recursively validate the left and right subtrees
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        # Start the validation from the root with no bounds
        return validate(root)

def insert_level_order(arr, root, i, n):
    """Helper function to insert nodes in level order."""
    if i < n and arr[i] is not None:  # Check for None values
        temp = TreeNode(arr[i])
        root = temp

        # insert left child
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

        # insert right child
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)

    return root

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
root1_list = [2, 1, 3]
root1 = insert_level_order(root1_list, None, 0, len(root1_list))
print("Example 1:")
print("Input:", root1_list)
output1 = sol.isValidBST(root1)
print("Output:", output1)

# Example 2
print("=".center(50, "="))
root2_list = [5 ,1 ,4 , None, None,3,6]
root2 = insert_level_order(root2_list, None, 0, len(root2_list))
print("Example 2:")
print("Input:", root2_list)
output2 = sol.isValidBST(root2)
print("Output:", output2)
print("=".center(50, "="))
