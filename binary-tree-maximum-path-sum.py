# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return float('-inf')

            left = dfs(node.left)
            right = dfs(node.right)
            left = 0 if left < 0 else left
            right = 0 if right < 0 else right
            include_node = left + right + node.val
            dfs.result = max(dfs.result, include_node)
            return max(left + node.val, right + node.val)

        if not root:
            return 0

        dfs.result = float('-inf')
        dfs(root)
        return dfs.result
