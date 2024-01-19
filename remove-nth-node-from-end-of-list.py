# One pass
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = n
        def helper(node):
            nonlocal N
            if not node or not node.next:
                return node
        
            curr = helper(node.next)
            N -= 1
            if N == 0:
                node.next = node.next.next
            return head

        dummy = ListNode(-1, head)
        helper(dummy)
        return dummy.next
        