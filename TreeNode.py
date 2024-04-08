class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Insert a new node with the given key into the binary search tree.
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Perform preorder traversal of the binary search tree.
def preorder_traversal(root):
    if root:
        print(root.val, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Perform inorder traversal of the binary search tree.
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

# Perform postorder traversal of the binary search tree.
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=' ')


if __name__ == "__main__":
    root = None
    keys = [10, 5, 15, 3, 8, 12, 18]

    for key in keys:
        root = insert(root, key)

    print("Preorder traversal:")
    preorder_traversal(root)
    print("\nInorder traversal:")
    inorder_traversal(root)
    print("\nPostorder traversal:")
    postorder_traversal(root)
