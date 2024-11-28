from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # If the head is None or left equals right, no need to reverse
        if not head or left == right:
            return head
        
        # Create a dummy node that points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move `prev` to the node just before the `left` position
        for _ in range(left - 1):
            prev = prev.next
        
        # Start reversing from the `left` position

        # This is the first node to reverse
        reverse_start = prev.next  
        # This will be used to iterate and reverse
        curr = reverse_start.next   
        
        # Reverse the nodes from `left` to `right`
        for _ in range(right - left):
            # Link current start to the next node
            reverse_start.next = curr.next  
            # Link current node to the start of reversed section
            curr.next = prev.next            
            # Move current node to the front of reversed section
            prev.next = curr                 
            # Move to the next node to be reversed
            curr = reverse_start.next        
        
        # Return the new head of the list
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(elements):
    dummy = ListNode(0)
    current = dummy
    for value in elements:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert a linked list back to a Python list for easy output comparison
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
head1 = create_linked_list([1, 2, 3, 4, 5])
left1 = 2
right1 = 4
print("Example 1:")
print("Input:", linked_list_to_list(head1))
output1 = sol.reverseBetween(head1, left1, right1)
print("Output:", linked_list_to_list(output1))
print("=".center(50, "="))

# Example 2
head2 = create_linked_list([5])
left2 = 1
right2 = 1
print("Example 2:")
print("Input:", linked_list_to_list(head2))
output2 = sol.reverseBetween(head2, left2, right2)
print("Output:", linked_list_to_list(output2))
print("=".center(50, "="))