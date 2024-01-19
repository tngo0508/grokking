# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        no_cycle = True
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                no_cycle = False
                break
        
        if no_cycle:
            return

        p1 = slow
        p2 = head
        while p1 and p2:
            if p1 is p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        
        return
        
        