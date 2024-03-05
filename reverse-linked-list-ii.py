# My solution - accepted
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left is right:
            return head
        dummy = ListNode(-1, head)
        prev_left = curr = head
        left_node = right_node = None
        prev = dummy
        next_right = None
        count = 1

        while curr:
            if count == left:
                left_node = curr
                prev_left = prev
            if count == right:
                right_node = curr
                next_right = curr.next
            
            prev = curr
            curr = curr.next
            count += 1
        
        prev = None
        curr = left_node
        right_node.next = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        prev_left.next, left_node.next = right_node, next_right

        return dummy.next