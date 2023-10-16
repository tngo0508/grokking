# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode

class Solution:
    def lowest_common_ancestor(self, current_node, p, q):
        def dfs(root, p, q):
            if not root:
                return False

            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            left_found = True if left else False
            right_found = True if right else False

            found = root is p or root is q

            if left_found + right_found + found >= 2:
                return root

            return left or right or found



        return dfs(current_node, p, q)
    
#Solution
from BinaryTree import *

class Solution:
    def __init__(self):
        self.lca = None

    def lowest_common_ancestor(self, root, p, q):
        self.lowest_common_ancestor_rec(root, p, q)
        return self.lca

    # helper function to find the lowest common ancestor recursively
    def lowest_common_ancestor_rec(self, current_node, p, q):
        # if current_node does not exist
        if not current_node:
            return False
        
        # initialize tracking variables
        left, right, mid = False, False, False

        # check if either of the input nodes is the current_node
        if p == current_node or q == current_node:
            mid = True
        
        # traverse binary tree using depth-first search
        left = self.lowest_common_ancestor_rec(current_node.left, p, q)

        # if the lowest common ancestor has not been found, only then traverse the right subtree
        if not self.lca:
            right = self.lowest_common_ancestor_rec(current_node.right, p, q)

        # if any two of the tracking variables are true, set current_node as answer node
        if mid + left + right >= 2:
            self.lca = current_node
        
        # return true if any of the tracking variables is true
        return mid or left or right

# driver code    
def main():
    input_trees = [[TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(350)],
        [TreeNode(100), TreeNode(200), TreeNode(75), TreeNode(50), TreeNode(25), TreeNode(350)],
        [TreeNode(350), TreeNode(100), TreeNode(75), TreeNode(50), TreeNode(200), TreeNode(25)],
        [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(350)],
        [TreeNode(25), TreeNode(50), TreeNode(75), TreeNode(100), TreeNode(200), TreeNode(350)]]
    
    input_nodes = [
        [25, 75],
        [50, 350],
        [100, 200],
        [50, 25],
        [350, 200]
    ]

    for i in range(len(input_trees)):
        solution = Solution()
        tree = BinaryTree(input_trees[i])
        print(i+1, ".\tBinary tree:", sep="")
        display_tree(tree.root)
        print("\tp = ", input_nodes[i][0])
        print("\tq = ", input_nodes[i][1])
        lca = solution.lowest_common_ancestor(tree.root, tree.find(input_nodes[i][0]), tree.find(input_nodes[i][1]))
        print("\n\tLowest common ancestor: ", lca.data, sep="")
        print("-"*100)

if __name__ == "__main__":
    main()