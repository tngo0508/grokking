# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = self.get_leaves(root1)
        l2 = self.get_leaves(root2)

        if len(l1) != len(l2):
            return False

        for n1, n2 in zip(l1, l2):
            if n1 != n2:
                return False
        return True

    def get_leaves(self, node):
        if not node:
            return []

        if not node.left and not node.right:
            return [node.val]
        
        result = []
        result += self.get_leaves(node.left)
        result += self.get_leaves(node.right)
        return result


# Editorial solution
class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))