from ds_v1.BinaryTree.BinaryTree import TreeNode
# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

def dfs(root):
  if not root:
    return 0, 0

  diameter, left_depth = dfs(root.left)
  diameter, right_depth = dfs(root.right)
  return (max(diameter, left_depth + right_depth), max(left_depth, right_depth) + 1)

def diameter_of_binaryTree(root):
  diameter, depth = dfs(root)
  return diameter
