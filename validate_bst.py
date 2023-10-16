# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode
import math

def dfs(root, lower_bound, upper_bound):
    if not root:
        return True

    if not (lower_bound < root.data < upper_bound):
        return False

    return dfs(root.left, lower_bound, root.data) and dfs(root.right, root.data, upper_bound)

def validate_bst(root):
    return dfs(root, float('-inf'), float('inf'))
