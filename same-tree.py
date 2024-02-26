# Brute force - accepted
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder_travesal(node, curr):
            if not node:
                curr.append(None)
                return
            
            curr.append(node.val)
            preorder_travesal(node.left, curr)
            preorder_travesal(node.right, curr)

        p_list, q_list = [], []
        preorder_travesal(p, p_list)
        preorder_travesal(q, q_list)
        return p_list == q_list

# Traverse the two tree simultaneously
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and not q:
            return False
        if not p and q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
