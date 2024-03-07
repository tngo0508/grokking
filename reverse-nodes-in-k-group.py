# Stack Approach - Accepted
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        dummy = ListNode(-1)
        curr = head
        prev = dummy
        while curr:
            stack.append(curr)
            curr = curr.next
            if len(stack) == k:
                group_prev = prev
                while stack:
                    node = stack.pop()
                    group_prev.next = node
                    group_prev = node
                group_prev.next = curr
                prev = group_prev
        
        return dummy.next
            
# Other approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = []
        curr = head
        while curr:
            temp.append(curr)
            curr = curr.next
        
        for i in range(0, len(temp), k):
            l, r = i, i + k - 1
            if r >= len(temp):
                break
            while l < r:
                temp[l], temp[r] = temp[r], temp[l]
                l += 1
                r -= 1
        
        for i in range(len(temp) - 1):
            temp[i].next = temp[i + 1]

        if temp:
            temp[-1].next = None
        
        return temp[0] if temp else None