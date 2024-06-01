# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes 
# (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        # Create a dummy node that will act as the starting point of the modified list
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize a pointer to track the previous node, starting from the dummy
        prev_node = dummy
        
        # Traverse the list while there are at least two more nodes to process
        while head and head.next:
            # Identify the first and second nodes to be swapped
            first_node = head
            second_node = head.next
            
            # Perform the swap
            # Point the previous node to the second node
            prev_node.next = second_node   
            # Link the first node to the node after the second node
            first_node.next = second_node.next  
            # Link the second node to the first node
            second_node.next = first_node  
            
            # Move the prev_node and head pointers two nodes ahead
            prev_node = first_node
            head = first_node.next
        
        # Return the new head node, which is the next node after the dummy
        return dummy.next

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
head1 = list_to_linkedlist([1, 2, 3, 4])
print("Example 1:", end=" ")
print_linkedlist(sol.swapPairs(head1))
print("=".center(50, "="))

# Example 2
head2 = list_to_linkedlist([])
print("Example 2:", end=" ")
print_linkedlist(sol.swapPairs(head2))
print("=".center(50, "="))

# Example 3
head3 = list_to_linkedlist([1])
print("Example 3:", end=" ")
print_linkedlist(sol.swapPairs(head3))
print("=".center(50, "="))
