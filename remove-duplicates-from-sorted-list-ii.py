# My solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101, head)
        prev = dummy
        freq = defaultdict(int)
        curr = head
        while curr:
            freq[curr.val] += 1
            curr = curr.next
        
        curr = head
        while curr:
            if freq[curr.val] > 1:
                curr = curr.next
                prev.next = None
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
     
        return dummy.next