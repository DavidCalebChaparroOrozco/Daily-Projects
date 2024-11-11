# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x: int):
        # Create two dummy nodes to serve as the heads of the two partitions
        less_head = ListNode(0)  # Dummy head for the 'less' partition
        greater_head = ListNode(0)  # Dummy head for the 'greater or equal' partition
        
        # Pointers to build the two partitions
        less = less_head
        greater = greater_head
        
        # Iterate through the original linked list
        current = head
        while current:
            if current.val < x:
                # If current node's value is less than x, add it to 'less' partition
                less.next = current
                less = less.next  # Move the pointer forward in 'less' partition
            else:
                # If current node's value is greater than or equal to x, add it to 'greater' partition
                greater.next = current
                greater = greater.next  # Move the pointer forward in 'greater' partition
            
            # Move to the next node in the original list
            current = current.next
        
        # Connect the end of 'less' partition to the head of 'greater' partition
        less.next = greater_head.next
        
        # Ensure the last node of 'greater' points to None
        greater.next = None
        
        # Return the head of the 'less' partition, which is next to the dummy head
        return less_head.next

# Helper function to convert a list to a ListNode
def list_to_linkedlist(items):
    dummy = ListNode(0)
    current = dummy
    for item in items:
        current.next = ListNode(item)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linkedlist(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    return elements

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
head1 = list_to_linkedlist([1,4,3,2,5,2])
x1 = 3
print("Example 1:")
print("Input:", [1, 4, 3, 2, 5, 2])
output1 = sol.partition(head1, x1)
print("Output:", print_linkedlist(output1))
print("=".center(50,"="))

# Example 2
head2 = list_to_linkedlist([2,1])
x2 = 2
print("Example 2:")
print("Input:", [2, 1])
output2 = sol.partition(head2, x2)
print("Output:", print_linkedlist(output2))
print("=".center(50,"="))
