# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0, head)
        # 'prev' is the last node before the duplicates
        prev = dummy

        # Traverse the linked list
        while head:
            # Check if the current node is the start of a sequence of duplicates
            if head.next and head.val == head.next.val:
                # Move head forward until the end of duplicates
                while head.next and head.val == head.next.val:
                    head = head.next
                # Link prev to the node after the last duplicate
                prev.next = head.next
            else:
                # No duplicate, move prev to the current node
                prev = prev.next

            # Move head to the next node
            head = head.next

        # Return the new head of the list
        return dummy.next

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
head1 = create_linked_list([1, 2, 3, 3, 4, 4, 5])
result1 = sol.deleteDuplicates(head1)
print("Example 1:", linked_list_to_list(result1))
print("=".center(50, "="))

# Example 2
head2 = create_linked_list([1, 1, 1, 2, 3])
result2 = sol.deleteDuplicates(head2)
print("Example 2:", linked_list_to_list(result2))
print("=".center(50, "="))