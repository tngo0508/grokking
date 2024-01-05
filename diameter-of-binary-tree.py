# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def find_depth(node):
            if not node:
                return 0
            
            left_sub_tree = find_depth(node.left)
            right_sub_tree = find_depth(node.right)
            
            find_depth.result = max(left_sub_tree + right_sub_tree, find_depth.result)

            return max(left_sub_tree, right_sub_tree) + 1

        find_depth.result = 0
        find_depth(root)
        return find_depth.result