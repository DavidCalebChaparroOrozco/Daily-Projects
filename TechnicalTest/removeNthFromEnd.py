# Given the head of a linked list, remove the nth node from the end of the 
# list and return its head.


# Define ListNode class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Create a dummy node to handle the case where the node to be removed is the first one
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move the first pointer ahead by n+1 positions
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until the first pointer reaches the end of the list
        while first is not None:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        second.next = second.next.next
        
        return dummy.next

# Function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
head1 = create_linked_list([1,2,3,4,5])
n1 = 2
print("Example 1:")
print("Input:", linked_list_to_list(head1))
result1 = sol.removeNthFromEnd(head1, n1)
print("Output:", linked_list_to_list(result1))
print("=".center(50,"="))

# Example 2
head2 = create_linked_list([1])
n2 = 1
print("Example 2:")
print("Input:", linked_list_to_list(head2))
result2 = sol.removeNthFromEnd(head2, n2)
print("Output:", linked_list_to_list(result2))
print("=".center(50,"="))

# Example 3
head3 = create_linked_list([1,2])
n3 = 1
print("Example 3:")
print("Input:", linked_list_to_list(head3))
result3 = sol.removeNthFromEnd(head3, n3)
print("Output:", linked_list_to_list(result3))
print("=".center(50,"="))
