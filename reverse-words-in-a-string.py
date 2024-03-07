# My solution
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        N = len(s)
        curr = []
        for i in reversed(range(N)):
            if not s[i].isalnum() and curr:
                res.append(''.join(curr[::-1]))
                curr = []
            
            if s[i].isalnum():
                curr.append(s[i])
        
        if curr:
            res.append(''.join(curr[::-1]))
        return ' '.join(res)
    
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
