# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Importing necessary libraries
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        # Min-heap to keep track of the smallest elements across the k lists
        min_heap = []

        # Initialize the heap with the head node of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        # Dummy head for the result list
        dummy = ListNode(0)
        current = dummy
        
        # While there are elements in the heap
        while min_heap:
            # Get the smallest element
            val, idx, node = heapq.heappop(min_heap)  
            # Add this smallest element to the result list
            current.next = ListNode(val)  
            # Move to the next node in the result list
            current = current.next  
            
            # If the popped node has a next node, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        
        # Return the merged sorted list
        return dummy.next

# Helper function to convert list of lists to list of ListNode
def build_linked_lists(arrays):
    lists = []
    for array in arrays:
        if not array:
            lists.append(None)
            continue
        head = ListNode(array[0])
        current = head
        for value in array[1:]:
            current.next = ListNode(value)
            current = current.next
        lists.append(head)
    return lists

# Helper function to print linked list
def print_linked_list(node):
    if not node:
        print("[]")
        return
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
example1 = [[1,4,5], [1,3,4], [2,6]]
print("Example 1:")
print("Input:", example1)
lists1 = build_linked_lists(example1)
merged1 = sol.mergeKLists(lists1)
print("Merged List:")
print_linked_list(merged1)

# Example 2
print("=".center(50, "="))
example2 = []
print("Example 2:")
print("Input:", example2)
lists2 = build_linked_lists(example2)
merged2 = sol.mergeKLists(lists2)
print("Merged List:")
print_linked_list(merged2)

# Example 3
print("=".center(50, "="))
example3 = [[]]
print("Example 3:")
print("Input:", example3)
lists3 = build_linked_lists(example3)
merged3 = sol.mergeKLists(lists3)
print("Merged List:")
print_linked_list(merged3)
print("=".center(50, "="))