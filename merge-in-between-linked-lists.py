# My solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node_a = node_b = None
        curr = list1
        i = 0
        while curr is not None:
            if i == a - 1:
                node_a = curr
            if i == b + 1:
                node_b = curr
            curr = curr.next
            i += 1
        
        node_a.next = list2
        curr = list2
        while curr is not None and curr.next is not None:
            curr = curr.next
        
        curr.next = node_b

        return list1
        
            
        
        
