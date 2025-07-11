# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, intersectVal: int, listA: list, listB: list, skipA: int, skipB: int) -> ListNode:
        # Helper function to create a linked list from a list and stop at a certain index
        def create_linked_list(lst, stop_index):
            if not lst:
                return None
            head = ListNode(lst[0])
            current = head
            for i in range(1, len(lst)):
                if i == stop_index:
                    # Link to the intersection node if it exists
                    intersection_node = ListNode(lst[i])
                    current.next = intersection_node
                    current = intersection_node
                    # The rest of the list is shared, so we break here
                    break
                else:
                    current.next = ListNode(lst[i])
                    current = current.next
            return head, current if stop_index < len(lst) else None

        # Create the linked lists up to the skip indices
        headA, tailA = create_linked_list(listA, skipA)
        headB, tailB = create_linked_list(listB, skipB)

        # Link the tails to the intersection node if it exists
        if tailA and tailB:
            # The intersection node is the node at skipA in listA and skipB in listB
            # Since the lists are constructed the same way after skipA and skipB
            # We can just link tailA and tailB to the same node
            intersection_node = ListNode(listA[skipA])
            tailA.next = intersection_node
            tailB.next = intersection_node

        # Now, find the intersection node using the two-pointer technique
        if not headA or not headB:
            return None

        ptrA = headA
        ptrB = headB

        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA

        return ptrA

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
intersectVal1 = 8
listA1 = [4, 1, 8, 4, 5]
listB1 = [5, 6, 1, 8, 4, 5]
skipA1 = 2
skipB1 = 3
print("Example 1:")
print("Input:", intersectVal1)
print("Output:", sol.getIntersectionNode(intersectVal1, listA1, listB1, skipA1, skipB1).val if sol.getIntersectionNode(intersectVal1, listA1, listB1, skipA1, skipB1) else None)
print("=".center(50,"="))

# Example 2
intersectVal2 = 2
listA2 = [1, 9, 1, 2, 4]
listB2 = [3, 2, 4]
skipA2 = 3
skipB2 = 1
print("Example 2:")
print("Input:", intersectVal2)
print("Output:", sol.getIntersectionNode(intersectVal2, listA2, listB2, skipA2, skipB2).val if sol.getIntersectionNode(intersectVal2, listA2, listB2, skipA2, skipB2) else None)
print("=".center(50,"="))

# Example 3
intersectVal3 = 0
listA3 = [2, 6, 4]
listB3 = [1, 5]
skipA3 = 3
skipB3 = 2
print("Example 3:")
print("Input:", intersectVal3)
print("Output:", sol.getIntersectionNode(intersectVal3, listA3, listB3, skipA3, skipB3).val if sol.getIntersectionNode(intersectVal3, listA3, listB3, skipA3, skipB3) else None)
print("=".center(50,"="))