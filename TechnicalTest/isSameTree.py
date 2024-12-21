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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # If both nodes are None, the trees are the same up to this point
        if not p and not q:
            return True
        
        # If one of the nodes is None and the other is not, trees are not the same
        if not p or not q:
            return False
        
        # If the values of the current nodes are different, trees are not the same
        if p.val != q.val:
            return False
        
        # Recursively check the left subtree and right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

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

# Example 1
print("=".center(50,"="))
p1 = [1, 2, 3]
q1 = [1, 2, 3]
tree1 = buildTreeFromList(p1)
tree2 = buildTreeFromList(q1)
print("Example 1:")
print("Input:", p1, " ", q1)
print("Output:", sol.isSameTree(tree1, tree2))
print("=".center(50,"="))

# Example 2
p2 = [1, 2]
q2 = [1, None, 2]
tree3 = buildTreeFromList(p2)
tree4 = buildTreeFromList(q2)
print("Example 2:")
print("Input:", p2, " ", q2)
print("Output:", sol.isSameTree(tree3, tree4))
print("=".center(50,"="))

# Example 3
p3 = [1, 2, 1]
q3 = [1, 1, 2]
tree5 = buildTreeFromList(p3)
tree6 = buildTreeFromList(q3)
print("Example 3:")
print("Input:", p3)
print("Output:", sol.isSameTree(tree5, tree6))
print("=".center(50,"="))
