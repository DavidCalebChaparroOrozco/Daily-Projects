# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Perform postorder traversal of a binary tree iteratively.
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        """
        Args:
            root: Root node of the binary tree
            
        Returns:
            List of node values in postorder traversal order
        """
        # Initialize an empty list to store the traversal result
        result = []
        
        # Initialize a stack to help with iterative traversal
        stack = []
        
        # Start from the root node
        current = root
        last_visited = None
        
        # Continue traversal while there are nodes to process
        while current or stack:
            # Go all the way to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Peek at the top of the stack
            peek_node = stack[-1]
            
            # If right child exists and hasn't been visited yet
            if peek_node.right and peek_node.right != last_visited:
                current = peek_node.right
            else:
                # Process the node (left and right subtrees done)
                result.append(peek_node.val)
                last_visited = stack.pop()
                
        return result
    
# Helper function to build tree from list representation
def build_tree(nodes):
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    
    while queue and i < len(nodes):
        current = queue.pop(0)
        
        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    
    return root

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
nodes1 = [1, None, 2, 3]
root1 = build_tree(nodes1)
print("Example 1:")
print("Input:", nodes1)
print("Output:", sol.postorderTraversal(root1))
print("=".center(50,"="))

# Example 2
nodes2 = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, None, None, 9]
root2 = build_tree(nodes2)
print("Example 2:")
print("Input:", nodes2)
print("Output:", sol.postorderTraversal(root2))
print("=".center(50,"="))

# Example 3
nodes3 = []
root3 = build_tree(nodes3)
print("Example 3:")
print("Input:", nodes3)
print("Output:", sol.postorderTraversal(root3))
print("=".center(50,"="))

# Example 4
nodes4 = [1]
root4 = build_tree(nodes4)
print("Example 4:")
print("Input:", nodes4)
print("Output:", sol.postorderTraversal(root4))
print("=".center(50,"="))