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
    def isSymmetric(self, root) -> bool:
        # A tree is symmetric if it is empty or if its left and right subtrees are mirrors of each other
        if not root:
            return True
        
        # Helper function to compare two nodes
        def isMirror(t1: TreeNode, t2: TreeNode) -> bool:
            # If both nodes are None, they are symmetric
            if not t1 and not t2:
                return True
            
            # If one of the nodes is None, they are not symmetric
            if not t1 or not t2:
                return False
            
            # Check if the current nodes' values are equal and recursively check their children
            return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        # Start the comparison from the root's left and right children
        return isMirror(root.left, root.right)

# Helper function to insert nodes in level order.
def insertLevelOrder(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        # insert left child
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root

# Builds a binary tree from a list.
def buildTreeFromList(lst):
    if not lst:
        return None
    return insertLevelOrder(lst, None, 0, len(lst))

# Create an instance of the Solution class
sol = Solution()

# Example 1: Symmetric Tree
root1 = [1, 2, 2, 3, 4, 4, 3]
tree1 = buildTreeFromList(root1)
print("=".center(50,"="))
print("Example 1:")
print("Input:", root1)
print("Output:", sol.isSymmetric(tree1))  
print("=".center(50,"="))

# Example 2: Asymmetric Tree
root2 = [1, 2, 2, None, 3, None, 3]
tree2 = buildTreeFromList(root2)
print("Example 2:")
print("Input:", root2)
print("Output:", sol.isSymmetric(tree2)) 
print("=".center(50,"="))
