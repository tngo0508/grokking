# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        queue = deque([root])
        result = []
        while queue:
            n = len(queue)
            result.append([])
            for _ in range(n):
                node = queue.popleft()
                if node:
                    result[-1].append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return result

