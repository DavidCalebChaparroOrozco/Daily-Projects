# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list into two halves
        second_half = slow.next
        slow.next = None
        
        # Step 2: Reverse the second half
        prev = None
        current = second_half
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        second_half = prev
        
        # Step 3: Merge the two halves alternately
        first_half = head
        while second_half:
            temp1 = first_half.next
            temp2 = second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half = temp1
            second_half = temp2

# Helper function to print the linked list for testing purposes
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example usage
sol = Solution()

# Example 1
print("=".center(50, "="))
head1 = create_linked_list([1, 2, 3, 4])
print("Example 1:")
print("Original list:")
print_linked_list(head1)
sol.reorderList(head1)
print("Reordered list:")
print_linked_list(head1)
print("=".center(50, "="))

# Example 2
head2 = create_linked_list([1, 2, 3, 4, 5])
print("Example 2:")
print("Original list:")
print_linked_list(head2)
sol.reorderList(head2)
print("Reordered list:")
print_linked_list(head2)
print("=".center(50, "="))