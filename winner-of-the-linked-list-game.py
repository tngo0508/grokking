# Brute force
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        points = defaultdict()
        points["odd"] = 0
        points["even"] = 0
        curr = head
        while curr and curr.next:
            even_idx_val = curr.val
            odd_idx_val = curr.next.val
            if odd_idx_val > even_idx_val:
                points["odd"] += 1
            elif odd_idx_val < even_idx_val:
                points["even"] += 1
            curr = curr.next.next
        
        if points["odd"] > points["even"]:
            return "Odd"
        elif points["odd"] < points["even"]:
            return "Even"
        
        return "Tie"
