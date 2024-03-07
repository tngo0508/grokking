# My solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        q = deque()
        curr = head
        while curr:
            q.append(curr)
            curr = curr.next

        if not q:
            return
        
        n = len(q)
        for _ in range(k % n):
            node = q.pop()
            q.appendleft(node)
        
        dummy = ListNode(-1)
        curr = dummy
        while q:
            node = q.popleft()
            curr.next = node
            curr = curr.next
        
        curr.next = None
        
        return dummy.next