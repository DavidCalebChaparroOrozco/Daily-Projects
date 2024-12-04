# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # The value of the node
        self.val = val  
        # Pointer to the left child
        self.left = left  
        # Pointer to the right child
        self.right = right  

class Solution:
    def inorderTraversal(self, root) -> list[int]:
        # This list will hold the values of the nodes in inorder
        result = []
        
        # Helper function to perform the inorder traversal
        def traverse(node):
            # Check if the current node is not null
            if node is not None:  
                # Traverse the left subtree
                traverse(node.left)  
                # Visit the current node
                result.append(node.val)  
                # Traverse the right subtree
                traverse(node.right)  
        
        # Start the traversal from the root
        traverse(root)  
        # Return the list of values in inorder
        return result  

# Helper function to build a binary tree from a list.
def build_tree_from_list(values):
    if not values:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in values]
    child_index = 1
    
    for i in range(len(nodes)):
        if nodes[i] is not None:
            if child_index < len(nodes):
                nodes[i].left = nodes[child_index]
                child_index += 1
            if child_index < len(nodes):
                nodes[i].right = nodes[child_index]
                child_index += 1
    
    # The root of the tree
    return nodes[0]  

# Example usage
sol = Solution()

# Example 1
print("=".center(50, "="))
print("Example 1:")
root1 = [1, None, 2, 3]
tree1 = build_tree_from_list(root1)
output1 = sol.inorderTraversal(tree1)
print("Input:", root1)
print("Output:", output1)
print("=".center(50, "="))

# Example 2
print("Example 2:")
root2 = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
tree2 = build_tree_from_list(root2)
output2 = sol.inorderTraversal(tree2)
print("Input:", root2)
print("Output:", output2)
print("=".center(50, "="))

# Example 3
print("Example 3:")
root3 = []
tree3 = build_tree_from_list(root3)
output3 = sol.inorderTraversal(tree3)
print("Input:", root3)
print("Output:", output3)
print("=".center(50, "="))

# Example 4
print("Example 4:")
root4 = [1]
tree4 = build_tree_from_list(root4)
output4 = sol.inorderTraversal(tree4)
print("Input:", root4)
print("Output:", output4)
print("=".center(50, "="))