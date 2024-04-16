# Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# 2 -> 4 -> 3
# 5 -> 6 -> 4
# -----------
# 7 -> 0 -> 8

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:
#   The number of nodes in each linked list is in the range [1, 100].
#   0 <= Node.val <= 9
#   It is guaranteed that the list represents a number that does not have leading zeros.


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Create a dummy node to store the result
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Traverse both linked lists simultaneously
        while l1 or l2:
            # Get the values of the current nodes, or 0 if node is None
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Calculate sum and carry
            sum_val = x + y + carry
            carry = sum_val // 10
            sum_val %= 10
            
            # Create a new node with the sum value
            current.next = ListNode(sum_val)
            current = current.next

            # Move to the next nodes if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # Handle any final carry
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the head of the resulting linked list
        return dummy.next
