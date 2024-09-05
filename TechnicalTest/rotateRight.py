# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # If the list is empty or has only one node, no need to rotate
        if not head or not head.next or k == 0:
            return head

        # Initialize pointers and find the length of the linked list
        current = head
        # Start with 1 since we're already at the head
        length = 1  

        # Traverse the list to find its length and connect the last node to the head (make it circular)
        while current.next:
            current = current.next
            length += 1
        
        # Connect the last node to the head to form a circular list
        current.next = head

        # Find the actual number of rotations needed (mod by length to handle large k)
        k = k % length
        
        # Find the new tail position (length - k - 1) and new head position (length - k)
        steps_to_new_tail = length - k - 1
        new_tail = head

        # Traverse to the new tail
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # The new head will be the next node after the new tail
        new_head = new_tail.next

        # Break the circle by setting the new tail's next pointer to None
        new_tail.next = None

        # Return the new head of the rotated list
        return new_head

# Helper function to convert a Python list to a linked list
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a Python list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
head1 = [1, 2, 3, 4, 5]
k1 = 2
print("Example 1:")
print("Input:", head1)
linkedlist_head1 = list_to_linkedlist(head1)  
rotated_head1 = sol.rotateRight(linkedlist_head1, k1)  
output1 = linkedlist_to_list(rotated_head1)  
print("Output:", output1)

# Example 2
print("=".center(50, "="))
n2 = [0, 1, 2]
k2 = 4
print("Example 2:")
print("Input:", n2)
linkedlist_n2 = list_to_linkedlist(n2)  
rotated_n2 = sol.rotateRight(linkedlist_n2, k2)  
output2 = linkedlist_to_list(rotated_n2)  
print("Output:", output2)
print("=".center(50, "="))