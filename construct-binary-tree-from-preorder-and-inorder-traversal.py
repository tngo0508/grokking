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
    
# Editorial Solution
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            # if there are no elements to construct subtrees
            if in_left > in_right:
                return None
            
            # pick up the last element as a root
            val = postorder.pop()
            root = TreeNode(val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[val]
 
            # build the right subtree
            root.right = helper(index + 1, in_right)
            # build the left subtree
            root.left = helper(in_left, index - 1)
            return root
        
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)