# My Solution - BFS - queue - accepted
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque()
        queue.append(root)
        while queue:
            N = len(queue)
            for i in range(N):
                node = queue.popleft()
                next_node = queue[0] if i < N - 1 else None
                if node:
                    node.next = next_node
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return root
