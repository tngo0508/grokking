# Brute force
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0
        def helper(curr_node, ancestor_val):
            nonlocal result
            if not curr_node:
                return
            result = max(result, abs(ancestor_val - curr_node.val))
            helper(curr_node.left, ancestor_val)
            helper(curr_node.right, ancestor_val)

        def dfs(node):
            if not node:
                return

            helper(node, node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result
    
# DFS - cleaner code - improve approach
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node, curr_min, curr_max):
            nonlocal result
            if not node:
                return
            
            curr_min = min(curr_min, node.val)
            curr_max = max(curr_max, node.val)
            result = max(result, abs(curr_max - curr_min))
            dfs(node.left, curr_min, curr_max)
            dfs(node.right, curr_min, curr_max)

        dfs(root, root.val, root.val)
        return result

