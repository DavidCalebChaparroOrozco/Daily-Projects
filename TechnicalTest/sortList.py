# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        # Split the list into two halves
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        # Recursively sort each half
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)
        
        # Merge the sorted halves
        return self.merge(left_sorted, right_sorted)
    
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, left, right):
        dummy = ListNode()
        tail = dummy
        
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        
        if left:
            tail.next = left
        if right:
            tail.next = right
        
        return dummy.next

# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
head1 = [4, 2, 1, 3]
linked_head1 = list_to_linked_list(head1)
sorted_head1 = sol.sortList(linked_head1)
print("Example 1:")
print("Input:", head1)
print("Output:", linked_list_to_list(sorted_head1))
print("=".center(50, "="))

# Example 2
head2 = [-1, 5, 3, 4, 0]
linked_head2 = list_to_linked_list(head2)
sorted_head2 = sol.sortList(linked_head2)
print("Example 2:")
print("Input:", head2)
print("Output:", linked_list_to_list(sorted_head2))
print("=".center(50, "="))

# Example 3
head3 = []
linked_head3 = list_to_linked_list(head3)
sorted_head3 = sol.sortList(linked_head3)
print("Example 3:")
print("Input:", head3)
print("Output:", linked_list_to_list(sorted_head3))
print("=".center(50, "="))