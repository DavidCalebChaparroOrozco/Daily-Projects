# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Determines if a linked list has a cycle using Floyd's Tortoise and Hare algorithm.
    def hasCycle(self, head: ListNode) -> bool:
        """    
        Args:
            head: The head node of the linked list 
        Returns:
            bool: True if a cycle exists, False otherwise
        """
        # Initialize both pointers at the head of the list
        slow = head
        fast = head
        
        # Traverse the list until fast reaches the end
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by 1 step
            fast = fast.next.next     # Move fast pointer by 2 steps
            
            # If they meet, there's a cycle
            if slow == fast:
                return True
        
        # If we reach here, fast encountered None - no cycle
        return False

# Helper function to create a linked list from a list and pos
def create_linked_list(lst, pos):
    if not lst:
        return None
    nodes = [ListNode(val) for val in lst]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
head1 = [3, 2, 0, -4]
pos1 = 1
linked_list1 = create_linked_list(head1, pos1)
print("Example 1:")
print("Input head1:", head1, "pos:", pos1)
sol1 = sol.hasCycle(linked_list1)
print("Output:", sol1)
print("=".center(50, "="))

# Example 2
head2 = [1, 2]
pos2 = 0
linked_list2 = create_linked_list(head2, pos2)
print("Example 2:")
print("Input head2:", head2, "pos:", pos2)
sol2 = sol.hasCycle(linked_list2)
print("Output:", sol2)
print("=".center(50, "="))

# Example 3
head3 = [1]
pos3 = -1
linked_list3 = create_linked_list(head3, pos3)
print("Example 3:")
print("Input head3:", head3, "pos:", pos3)
sol3 = sol.hasCycle(linked_list3)
print("Output:", sol3)
print("=".center(50, "="))