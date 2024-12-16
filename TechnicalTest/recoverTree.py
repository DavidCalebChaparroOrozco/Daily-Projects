# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Do not return anything, modify root in-place instead.
    def recoverTree(self, root) -> None:
        # Initialize variables to keep track of the nodes
        self.first = None
        self.second = None
        self.prev = None

        # In-order traversal function to find the two swapped nodes
        def in_order_traversal(node):
            if not node:
                return

            # Traverse the left subtree
            in_order_traversal(node.left)

            # Identify the first and second swapped nodes
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    # First time finding a problem
                    self.first = self.prev  
                # Always update second when we find a problem
                self.second = node  

            # Update prev to the current node
            self.prev = node

            # Traverse the right subtree
            in_order_traversal(node.right)

        # Perform in-order traversal to find swapped nodes
        in_order_traversal(root)

        # Swap the values of the first and second nodes to correct the BST
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val

# Helper function to insert nodes in level order.
def insert_level_order(arr, root, i, n):
    # Check for None values
    if i < n and arr[i] is not None:  
        temp = TreeNode(arr[i])
        root = temp

        # insert left child
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

        # insert right child
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)

    return root

# Helper function to print in-order traversal.
def in_order_print(node):
    if not node:
        return
    in_order_print(node.left)
    print(node.val, end=" ")
    in_order_print(node.right)

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
root1_list = [1, 3, None, None, 2]
root1 = insert_level_order(root1_list, None, 0, len(root1_list))
print("Example 1:")
print("Input:", root1_list)
sol.recoverTree(root1)  
print("Output:", end=" ")
in_order_print(root1)
print("\n" + "="*50)

# Example 2
root2_list = [3, 1, 4, None, None, 2]
root2 = insert_level_order(root2_list, None, 0, len(root2_list))
print("Example 2:")
print("Input:", root2_list)
sol.recoverTree(root2) 
print("Output:", end=" ")
in_order_print(root2)
print("\n" + "="*50)
