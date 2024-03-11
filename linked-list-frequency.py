# My solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq_map = defaultdict(int)
        curr = head
        while curr:
            freq_map[curr.val] += 1
            curr = curr.next
        
        dummy = ListNode(-1)
        curr = dummy
        for v in freq_map.values():
            curr.next = ListNode(v)
            curr = curr.next
        
        return dummy.next
