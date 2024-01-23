# Stack Approach - Accepted
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        dummy = ListNode(-1)
        curr = head
        prev = dummy
        while curr:
            stack.append(curr)
            curr = curr.next
            if len(stack) == k:
                group_prev = prev
                while stack:
                    node = stack.pop()
                    group_prev.next = node
                    group_prev = node
                group_prev.next = curr
                prev = group_prev
        
        return dummy.next
            
        