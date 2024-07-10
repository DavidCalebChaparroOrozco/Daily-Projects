# Initialize a tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        """
        Args:
        value (int/str): The value of the node. It can be an integer (leaf node) or an operator (internal node).
        left (TreeNode): The left child node.
        right (TreeNode): The right child node.
        """
        self.value = value
        self.left = left
        self.right = right

# Evaluate the binary tree to compute the result of the expression it represents.
def evaluate_tree(root):
    """
    Args:
    root (TreeNode): The root node of the binary tree.

    Returns:
    int/float: The result of the expression.

    Raises:
    ValueError: If there is an attempt to divide by zero.
    """
    if root is None:
        return 0

    # If the node is a leaf, return its value
    if root.left is None and root.right is None:
        return root.value

    # Evaluate the left and right subtrees
    left_value = evaluate_tree(root.left)
    right_value = evaluate_tree(root.right)

    # Perform the corresponding operation
    if root.value == '+':
        return left_value + right_value
    elif root.value == '-':
        return left_value - right_value
    elif root.value == '*':
        return left_value * right_value
    elif root.value == '/':
        if right_value == 0:
            raise ValueError("Division by zero is not allowed.")
        return left_value / right_value
    elif root.value == '^':
        return left_value ** right_value

# Example usage

# Create a binary tree for the expression: ((3 + 2) * (4 - 1)) ^ 2
root = TreeNode('^')
root.left = TreeNode('*')
root.right = TreeNode(2)

root.left.left = TreeNode('+')
root.left.right = TreeNode('-')

root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(2)

root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(1)

# Evaluate the binary tree
result = evaluate_tree(root)
print("Result of the expression:", result)
