# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # Start with the head of the list
        current = head

        # Traverse the linked list
        while current and current.next:
            # If the current node has the same value as the next, skip the next node
            if current.val == current.next.val:
                # Skip duplicate node
                current.next = current.next.next  
            else:
                # Move to the next node if no duplicate
                current = current.next

        # Return the modified list head
        return head

# Helper function to create a linked list from a list
def create_linked_list(elements):
    dummy = ListNode(0)
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

# Helper function to convert linked list back to Python list for easy printing
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
head1 = create_linked_list([1, 1, 2])
result1 = sol.deleteDuplicates(head1)
print("Example 1:", linked_list_to_list(result1))
print("=".center(50, "="))

# Example 2
head2 = create_linked_list([1, 1, 2, 3, 3])
result2 = sol.deleteDuplicates(head2)
print("Example 2:", linked_list_to_list(result2))
print("=".center(50, "="))