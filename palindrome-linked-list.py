# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse_linked_list(node):
            prev = None
            curr = node
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            return prev


        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        p1 = head
        p2 = reverse_linked_list(slow)

        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True