# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Initialize two pointers, slow and fast
        slow = fast = head
        
        # First step: detect if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Cycle detected, now find the start of the cycle
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        # No cycle found
        return None

# Helper function to create a linked list with a cycle for testing purposes
def create_linked_list(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    nodes = [head]
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
        nodes.append(current)
    if pos != -1:
        current.next = nodes[pos]
    return head

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
head1 = [3, 2, 0, -4]
pos1 = 1
linked_list1 = create_linked_list(head1, pos1)
print("Example 1:")
print("Input head1:", head1, "pos:", pos1)
sol1 = sol.detectCycle(linked_list1)
print("Output:", sol1.val if sol1 else "null")
print("=".center(50, "="))

# Example 2
head2 = [1, 2]
pos2 = 0
linked_list2 = create_linked_list(head2, pos2)
print("Example 2:")
print("Input head2:", head2, "pos:", pos2)
sol2 = sol.detectCycle(linked_list2)
print("Output:", sol2.val if sol2 else "null")
print("=".center(50, "="))

# Example 3
head3 = [1]
pos3 = -1
linked_list3 = create_linked_list(head3, pos3)
print("Example 3:")
print("Input head3:", head3, "pos:", pos3)
sol3 = sol.detectCycle(linked_list3)
print("Output:", sol3.val if sol3 else "null")
print("=".center(50, "="))