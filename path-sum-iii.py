# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, target, curr_sum):
            if not node:
                return 0
            
            result = 0
            curr_sum += node.val
            if curr_sum == target:
                result += 1
            result += dfs(node.left, target, curr_sum)
            result += dfs(node.right, target, curr_sum)

            return result

        if not root:
            return 0
        
        ways = dfs(root, targetSum, 0)
        ways += self.pathSum(root.left, targetSum)
        ways += self.pathSum(root.right, targetSum)
        return ways