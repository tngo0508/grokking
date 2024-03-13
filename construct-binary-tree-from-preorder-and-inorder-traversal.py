# My Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        N = len(preorder)
        def build(arr):
            if build.index >= N or not arr:
                return

            val = preorder[build.index]
            root = TreeNode(preorder[build.index])
            i = arr.index(val)
            build.index += 1
            root.left = build(arr[:i])
            root.right = build(arr[i + 1:])

            return root

        build.index = 0
        return build(inorder)