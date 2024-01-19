"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = defaultdict()
        curr = head
        while curr:
            hash_map[curr] = Node(curr.val)
            curr = curr.next
        
        dummy = Node(-1)
        p = dummy
        curr = head
        while curr:
            p.next = hash_map[curr]
            p = p.next
            if curr.next in hash_map:
                p.next = hash_map[curr.next]
            if curr.random in hash_map:
                p.random = hash_map[curr.random]
            curr = curr.next

        return dummy.next