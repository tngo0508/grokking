# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, sub_node):
            if not node and not sub_node:
                return True
            if not node and sub_node:
                return False
            if node and not sub_node:
                return False
            if node.val != sub_node.val:
                return False
            return dfs(node.left, sub_node.left) and dfs(node.right, sub_node.right)
        
        def find_target(node, target, list_nodes):
            if not node:
                return
            if node.val == target.val:
                list_nodes.append(node)
            find_target(node.left, target, list_nodes)
            find_target(node.right, target, list_nodes)
        
        list_nodes = []
        find_target(root, subRoot, list_nodes)

        for node in list_nodes:
            if dfs(node, subRoot):
                return True
        return False
    
