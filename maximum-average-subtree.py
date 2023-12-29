# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        def dfs(root):
            if not root:
                return 0, 0
            L, count_left = dfs(root.left)
            R, count_right = dfs(root.right)
            count = count_left + count_right + 1
            dfs.result = max(dfs.result, (L + R + root.val) / count)
            return L + R + root.val, count

        dfs.result = 0
        dfs(root)
        return dfs.result 
