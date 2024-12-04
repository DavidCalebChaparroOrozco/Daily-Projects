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
    def generateTrees(self, n: int) -> list:
        # If n is 0, return an empty list as there are no trees
        if n == 0:
            return []
        
        # Dictionary to memoize results of subproblems
        memo = {}

        def generate_trees(start, end):
            # Check if the result for this range is already computed
            if (start, end) in memo:
                return memo[(start, end)]
            
            trees = []  # List to store all unique trees for this range
            
            # If start is greater than end, we return a list with None (no tree)
            if start > end:
                trees.append(None)
                return trees
            
            # Iterate through all possible root values
            for root_val in range(start, end + 1):
                # Generate all left subtrees using values less than root_val
                left_trees = generate_trees(start, root_val - 1)
                # Generate all right subtrees using values greater than root_val
                right_trees = generate_trees(root_val + 1, end)
            
                # Combine each left and right subtree with the current root
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        # Create a new tree with root_val as the root
                        root = TreeNode(root_val, left_tree, right_tree)
                        trees.append(root)  # Add the new tree to the list
            
            # Memoize the result before returning
            memo[(start, end)] = trees
            return trees

        # Generate trees using values from 1 to n
        return generate_trees(1, n)

# Function to serialize the tree into a list format for easy comparison and output
# Serialize tree into a list representation.
def serialize_tree(node):
    if not node:
        return None
    
    result = []
    
    def dfs(n):
        if n is None:
            result.append(None)
            return
        result.append(n.val)
        dfs(n.left)
        dfs(n.right)

    dfs(node)
    return result

# Example usage:
sol = Solution()

# Example 1
print("=".center(50, "="))
print("Example 1:")
input1 = 3
trees1 = sol.generateTrees(input1)
# Check if trees1 is None or empty before serializing
if trees1 is not None:
    output1 = [serialize_tree(tree) for tree in trees1]
else:
    output1 = []

print("Input:", input1)
print("Output:", output1)
print("=".center(50, "="))

# Example 2
print("Example 2:")
input2 = 1
trees2 = sol.generateTrees(input2)
# Check if trees2 is None or empty before serializing
if trees2 is not None:
    output2 = [serialize_tree(tree) for tree in trees2]
else:
    output2 = []
print("Input:", input2)
print("Output:", output2)
print("=".center(50, "="))