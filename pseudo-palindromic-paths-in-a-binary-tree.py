# Brute Force - accepted
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def helper(node, hash_map):
            if not node:
                return 0

            hash_map[node.val] += 1
            if node and (not node.left and not node.right):
                odd = 0
                for v in hash_map.values():
                    if v % 2 != 0:
                        odd += 1
                        if odd > 1:
                            return 0
                return 1
           
            L = helper(node.left, copy.deepcopy(hash_map))
            R = helper(node.right, copy.deepcopy(hash_map))
            return L + R

        return helper(root, defaultdict(int))