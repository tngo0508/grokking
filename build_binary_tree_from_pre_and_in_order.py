# Definition of a binary tree node
#
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode

def dfs(p_order, i_order):
    if dfs.p_index >= len(p_order) or not i_order:
        return None

    val = p_order[dfs.p_index]
    root = TreeNode(val)
    i_index = i_order.index(val)
    dfs.p_index += 1
    root.left = dfs(p_order, i_order[:i_index])
    root.right = dfs(p_order, i_order[i_index + 1:])
    return root


def build_tree(p_order, i_order):
    dfs.p_index = 0
    return dfs(p_order, i_order)

###SOLUTION
from TreeNode import *

def build_tree_helper(p_order, i_order, left, right, mapping, p_index):
    # if left > right, it means there are no more nodes left to construct
    if left > right:
        return None
 
    # Pick current node from preorder list
    # using p_index and increment p_index
    curr = p_order[p_index[0]]
    p_index[0] += 1
    root = TreeNode(curr)
 
    # If this node has no children then return
    if left == right:
        return root
 
    # Else find the index of this
    # node in inorder list
    in_index = mapping[curr]
    
    # Recursively build the left subtree by calling build_tree_helper
    # on the elements in the inorder list from left to in_index - 1
    root.left = build_tree_helper(p_order, i_order, left, in_index - 1, mapping, p_index)

    # Recursively build the right subtree by calling build_tree_helper
    # on the elements in the inorder list from in_index + 1 to right
    root.right = build_tree_helper(p_order, i_order, in_index + 1, right, mapping, p_index)
 
    return root
 
 
def build_tree(p_order, i_order):
    # Explicitly using List object to pass p_index by reference because
    # in python, Pass-by-object-reference is used and simple variable is not an object
    p_index = [0]
    # Using hash map to store the inorder list to reduce time complexity
    # of search to O(1)
    mapping = {}
    
    # Iterate through the inorder list and map each value to its index
    for i in range(len(p_order)):
        mapping[i_order[i]] = i
    
    return build_tree_helper(p_order, i_order, 0, len(p_order) - 1, mapping, p_index)

# Driver code
def main():
    
    p_order = [
        [3, 9, 20, 15, 7],
        [-1],
        [10, 20, 40, 50, 30, 60],
        [1, 2, 4, 5, 3, 6],
        [1, 2, 4, 7, 3],
        [1, 2, 4, 8, 9, 5, 3, 6, 7]
        
    ]
    
    i_order = [
        [9, 3, 15, 20, 7],
        [-1],
        [40, 20, 50, 10, 60, 30],
        [4, 2, 5, 1, 6, 3],
        [4, 2, 7, 1, 3],
        [8, 4, 9, 2, 5, 1, 6, 3, 7]
    ]
    
    indx = 0
    for i in range(len(p_order)):
        
        print(indx+1, ".\tPre order: ", p_order[indx], sep="")
        print("\tIn order: ", i_order[indx], sep="")
        tr = build_tree(p_order[indx], i_order[indx])
        indx += 1
        print("\n\tBinary tree:")
        display_tree(tr)
        print("-"*100)
        

if __name__ == '__main__':
    main()