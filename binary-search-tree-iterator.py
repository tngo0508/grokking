# My solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.dummy = TreeNode(-1)
        self.curr = self.dummy
        self.in_order_traverse(root)
        self.curr = self.dummy

    
    def in_order_traverse(self, root):
        if not root:
            return
        self.in_order_traverse(root.left)
        self.curr.right = root
        self.curr = self.curr.right
        self.in_order_traverse(root.right)

    def next(self) -> int:
        self.curr = self.curr.right
        return self.curr.val

    def hasNext(self) -> bool:
        return True if self.curr and self.curr.right else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()