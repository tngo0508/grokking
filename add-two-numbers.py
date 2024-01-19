# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while l1 and l2:
            sum_val = l1.val + l2.val + carry
            carry = sum_val // 10
            val = sum_val % 10 
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        node = l1 if l1 else l2
        while node:
            sum_val = node.val + carry
            carry = sum_val // 10
            val = sum_val % 10
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next

        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next