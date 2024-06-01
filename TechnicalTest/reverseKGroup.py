# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. 
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        # Function to reverse a part of the linked list
        def reverse_linked_list(head, k):
            prev = None
            curr = head
            while k:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev

        # Check if there are at least k nodes left to reverse
        node = head
        count = 0
        while count < k and node:
            node = node.next
            count += 1
        
        if count == k:
            # If we have k nodes, reverse them
            reversed_head = reverse_linked_list(head, k)
            # head is now the end of the reversed section, so its next should be the result of the recursive call
            head.next = self.reverseKGroup(node, k)
            return reversed_head
        
        # If we don't have k nodes, return head (no change)
        return head

# Utility function to convert a list into a linked list
def list_to_linkedlist(elements):
    dummy = ListNode(0)
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

# Utility function to print a linked list
def print_linkedlist(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(elements)

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
head1 = list_to_linkedlist([1, 2, 3, 4, 5])
k1 = 2
print("Example 1:", end=" ")
print_linkedlist(sol.reverseKGroup(head1, k1))
print("=".center(50, "="))

# Example 2
head2 = list_to_linkedlist([1,2,3,4,5])
k2 = 3
print("Example 2:", end=" ")
print_linkedlist(sol.reverseKGroup(head2, k2))
print("=".center(50, "="))
