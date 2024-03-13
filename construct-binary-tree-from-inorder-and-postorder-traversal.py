# My Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        N = len(inorder)
        postorder.reverse()


        def build(arr):
            if build.index >= N or not arr:
                return
            val = postorder[build.index]
            i = arr.index(val)
            root = TreeNode(val)
            build.index += 1
            root.right = build(arr[i+1:])
            root.left = build(arr[:i])
            return root
        
        build.index = 0
        return build(inorder)