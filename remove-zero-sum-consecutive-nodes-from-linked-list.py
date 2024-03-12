# My solution - accepted
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        stack = [[dummy, 0]]
        curr = head
        prefix_sum = {0}
        while curr:
            top, total = stack[-1]
            total += curr.val
            if total in prefix_sum:
                seen = total
                while stack and stack[-1][1] != seen:
                    top, total = stack.pop()
                    prefix_sum.remove(total)
            else:
                stack.append([curr, total])
                prefix_sum.add(total)
            curr = curr.next
        
        for i in range(len(stack) - 1):
            stack[i][0].next = stack[i + 1][0]
        
        stack[-1][0].next = None
        
        return stack[0][0].next