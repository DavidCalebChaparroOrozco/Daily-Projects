# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by 
# splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to act as the starting point of the merged list
        dummy = ListNode()
        current = dummy
        
        # Iterate through both lists while neither is empty
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # At least one of the lists is now empty
        # Append the remaining list to the end of the merged list
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        # Return the next node of the dummy, which is the head of the merged list
        return dummy.next

# Function to print the linked list
def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("Example 1:".center(50, "="))
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
merged_list = sol.mergeTwoLists(list1, list2)
print_list(merged_list)

# Example 2
print("Example 2:".center(50, "="))
list1 = create_linked_list([])
list2 = create_linked_list([])
merged_list = sol.mergeTwoLists(list1, list2)
print_list(merged_list)

# Example 3
print("Example 3:".center(50, "="))
list1 = create_linked_list([])
list2 = create_linked_list([0])
merged_list = sol.mergeTwoLists(list1, list2)
print_list(merged_list)