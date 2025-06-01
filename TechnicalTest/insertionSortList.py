# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):
        # Handle empty list or single node list
        if not head or not head.next:
            return head
        
        # Create a dummy node to serve as the starting point of the sorted list
        dummy = ListNode(0)
        dummy.next = head
        # 'last_sorted' points to the last node of the sorted part
        last_sorted = head
        # 'current' points to the node being considered for insertion
        current = head.next
        
        while current:
            if last_sorted.val <= current.val:
                # Current node is in the correct position, move last_sorted forward
                last_sorted = last_sorted.next
            else:
                # Need to find the correct position to insert current node
                prev = dummy
                # Find the insertion point
                while prev.next.val <= current.val:
                    prev = prev.next
                # Insert current node between prev and prev.next
                last_sorted.next = current.next
                current.next = prev.next
                prev.next = current
            # Move to the next node to be inserted
            current = last_sorted.next
        
        return dummy.next

    # Helper method to convert a list to a linked list
    def list_to_linkedlist(self, lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper method to convert a linked list to a list
    def linkedlist_to_list(self, head):
        lst = []
        current = head
        while current:
            lst.append(current.val)
            current = current.next
        return lst

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
head1 = [4,2,1,3]
print("Example 1:")
print("Input:", head1)
linked_head1 = sol.list_to_linkedlist(head1)
sorted_head1 = sol.insertionSortList(linked_head1)
output1 = sol.linkedlist_to_list(sorted_head1)
print("Output:", output1)
print("=".center(50,"="))

# Example 2
head2 = [-1,5,3,4,0]
print("Example 2:")
print("Input:", head2)
linked_head2 = sol.list_to_linkedlist(head2)
sorted_head2 = sol.insertionSortList(linked_head2)
output2 = sol.linkedlist_to_list(sorted_head2)
print("Output:", output2)
print("=".center(50,"="))