# BFS approach - Accepted
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def process_level(queue, is_even = True):
            prev = float('-inf') if is_even else float('inf')
            for _ in range(n):
                node = queue.popleft()
                if is_even:
                    if node.val % 2 != 0 and node.val > prev:
                        prev = node.val
                    else:
                        return False
                else:
                    if node.val % 2 == 0 and node.val < prev:
                        prev = node.val
                    else:
                        return False
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
            return True

        queue = deque()
        queue.append(root)
        level = 0
        while queue:
            n = len(queue)
            if level % 2 == 0:
                if not process_level(queue):
                    return False
            else:
                if not process_level(queue, is_even=False):
                    return False
            
            level += 1
        
        return True