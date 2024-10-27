# Define a class for the nodes in the binary tree

# Initialize the tree node
class TreeNode:
    def __init__(self, position, name):
        """
        Parameters:
            position: Position held in the organization.
            name: Name of the individual holding this position.
        """
        self.position = position
        self.name = name
        # Left child (e.g., a direct subordinate)
        self.left = None  
        # Right child (another direct subordinate)
        self.right = None  

# Define the Binary Tree class

# Initialize the organizational structure tree.
class OrgStructureTree:
    def __init__(self, root):
        """        
        Parameters:
            root: Root node representing the top-most position in the hierarchy.
        """
        self.root = root

    # Perform a pre-order traversal (visit node, then left, then right).
    def pre_order(self, node, visit):
        """    
        Parameters:
            node: Current node in the traversal.
            visit: Function to apply to each node during traversal.
        """
        if node:
            visit(node)
            self.pre_order(node.left, visit)
            self.pre_order(node.right, visit)

    # Perform an in-order traversal (visit left, node, then right).
    def in_order(self, node, visit):
        """        
        Parameters:
            node: Current node in the traversal.
            visit: Function to apply to each node during traversal.
        """
        if node:
            self.in_order(node.left, visit)
            visit(node)
            self.in_order(node.right, visit)

    # Perform a post-order traversal (visit left, right, then node).
    def post_order(self, node, visit):
        """        
        Parameters:
            node: Current node in the traversal.
            visit: Function to apply to each node during traversal.
        """
        if node:
            self.post_order(node.left, visit)
            self.post_order(node.right, visit)
            visit(node)

# Helper function to print node details

# Print the details of a node.
def print_node(node):
    """
    Parameters:
        node: Node to print.
    """
    print(f"Position: {node.position}, Name: {node.name}")

# Example usage: Building the company structure
# CEO -> COO (left), CTO (right) -> CTO has Dev Manager (left) and QA Manager (right)
if __name__ == "__main__":
    # Create nodes for each position
    ceo = TreeNode("CEO", "Caleb")
    coo = TreeNode("COO", "Fry")
    cto = TreeNode("CTO", "Turring")
    dev_manager = TreeNode("Development Manager", 'Bender')
    qa_manager = TreeNode("QA Manager", "Jhon Wick")

    # Establish relationships (tree structure)
    ceo.left = coo
    ceo.right = cto
    cto.left = dev_manager
    cto.right = qa_manager

    # Initialize the organizational structure tree
    company_tree = OrgStructureTree(ceo)

    # Traversals
    print("Pre-order Traversal (Management Hierarchy):")
    company_tree.pre_order(company_tree.root, print_node)

    print("\nIn-order Traversal (Detailed Structure):")
    company_tree.in_order(company_tree.root, print_node)

    print("\nPost-order Traversal (Team Completion):")
    company_tree.post_order(company_tree.root, print_node)
