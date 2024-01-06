# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        if not root.left:
            self.flatten(root.right)
        else:
            node = root.left
            while node and node.right:
                node = node.right
            
            node.right = root.right
            root.right, root.left = root.left, None
            self.flatten(root.right)
            
# Leet code solution
class Solution:
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # Handle the null scenario
        if not root:
            return None
        
        node = root
        while node:
            
            # If the node has a left child
            if node.left:
                
                # Find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            
            # move on to the right side of the tree
            node = node.right