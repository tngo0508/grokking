from ds_v1.BinaryTree.BinaryTree import TreeNode

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

def dfs(node, result, depth):
  if not node:
    return []

  if len(result) == depth:
    result.append(node.data)
  
  dfs(node.right, result, depth + 1)
  dfs(node.left, result, depth + 1)
  return result


def right_side_view(root):
  result = []
  if not root:
    return []
  
  return dfs(root, result, 0)

##Solution
def right_side_view(root):
    if root is None:
        return []

    rside = []
    dfs(root, 0, rside)

    return rside

# Apply depth-first search
def dfs(node, level, rside):
    if level == len(rside):
        rside.append(node.data)

    for child in [node.right, node.left]:
        if child: 
            dfs(child, level + 1, rside)