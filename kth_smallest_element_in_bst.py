# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
from ds_v1.BinaryTree.BinaryTree import TreeNode

def dfs(root):
    
    if root:
        dfs(root.left)
        dfs.k -= 1
        if dfs.k == 0 and dfs.node is not None:
            dfs.node = root
            return
        dfs(root.right)

def kth_smallest_element(root, k):
    dfs.node = root
    dfs.k = k
    dfs(root)
    return dfs.node.data
    
#####
from ds_v1.BinaryTree.BinaryTree import TreeNode

def kth_smallest_element(root: TreeNode, k: int) -> int:
    def dfs(node: TreeNode, k: int) -> TreeNode:
        if not node:
            return None
        
        left_result = dfs(node.left, k)
        if left_result:
            return left_result
        
        nonlocal count
        count -= 1
        if count == 0:
            return node
        
        return dfs(node.right, k)

    count = k
    result_node = dfs(root, k)
    return result_node.data if result_node else root.data


#########
from ds_v1.BinaryTree.BinaryTree import TreeNode

def kth_smallest_element(root: TreeNode, k: int) -> int:
    def dfs(node: TreeNode, k: int) -> TreeNode:
        if not node:
            return None, k
        
        left_result, k = dfs(node.left, k)
        if left_result:
            return left_result, k
        
        k -= 1
        if k == 0:
            return node, k
        
        right_result, k = dfs(node.right, k)
        return right_result, k

    result_node, _ = dfs(root, k)
    return result_node.data if result_node else root.data

####
from ds_v1.BinaryTree.BinaryTree import TreeNode

def kth_smallest_element(root: TreeNode, k: int) -> int:
    def dfs(node: TreeNode, remaining_k: int) -> TreeNode:
        if not node:
            return None, remaining_k
        
        left_result, remaining_k = dfs(node.left, remaining_k)
        if left_result:
            return left_result, remaining_k
        
        remaining_k -= 1
        if remaining_k == 0:
            return node, remaining_k
        
        return dfs(node.right, remaining_k)

    result_node, _ = dfs(root, k)
    return result_node.data if result_node else root.data