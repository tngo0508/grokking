# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                has_cycle = True
                break        

        if not has_cycle:
            return None

        slow = head
        while slow and fast:
            if slow is fast:
                break
            slow = slow.next
            fast = fast.next
        
        return slow