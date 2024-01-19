# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        curr = head
        prev = dummy
        while curr and curr.next:
            next_node = curr.next.next
            curr.next.next = curr
            prev.next = curr.next
            curr.next = next_node
            prev = curr
            curr = next_node
        
        return dummy.next
