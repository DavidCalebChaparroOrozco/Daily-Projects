# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Create a copy of each node and place it next to the original node
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        # Step 2: Assign random pointers for the copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # Step 3: Separate the copied list from the original list
        current = head
        copied_head = head.next
        copy_current = copied_head
        
        while current:
            current.next = current.next.next
            current = current.next
            if copy_current.next:
                copy_current.next = copy_current.next.next
                copy_current = copy_current.next
        
        return copied_head

# Helper function to create a linked list from a list of [val, random_index] pairs
def create_linked_list(nodes):
    if not nodes:
        return None
    # Create all nodes without setting next and random pointers
    node_list = [Node(val) for val, _ in nodes]
    # Set next pointers
    for i in range(len(node_list) - 1):
        node_list[i].next = node_list[i + 1]
    # Set random pointers
    for i, (_, random_idx) in enumerate(nodes):
        if random_idx is not None:
            node_list[i].random = node_list[random_idx]
    return node_list[0]

# Helper function to print the linked list (for testing purposes)
def print_linked_list(head):
    if not head:
        print("None")
        return
    # Create a list of nodes to map indices
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    # Print each node's val and random index
    output = []
    for node in nodes:
        if node.random:
            random_idx = nodes.index(node.random)
        else:
            random_idx = None
        output.append([node.val, random_idx])
    print(output)

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
nums1 = [2, 2, 1]
print("Example 1:")
print("Input nums1:", nums1)
sol1 = sol.singleNumber(nums1)
print("Output:", sol1)
print("=".center(50, "="))

# Example 2
nums2 = [1, 2, 2]
print("Example 2:")
print("Input nums2:", nums2)
sol2 = sol.singleNumber(nums2)
print("Output:", sol2)
print("=".center(50, "="))

# Example 3
num3 = [1]
print("Example 3:")
print("Input nums3:", num3)
sol3 = sol.singleNumber(num3)
print("Output:", sol3)
print("=".center(50, "="))