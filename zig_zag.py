from collections import deque
from ds_v1.BinaryTree.BinaryTree import TreeNode

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

def zigzag_level_order(root):
    if not root:
        return []
    q = deque([root])
    result = []
    left_to_right = False
    while q:
        n = len(q)
        curr = []
        for _ in range(n):
            node = q.popleft()
            curr.append(node.data)
            if node:
                if left_to_right:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
        if curr:
            result.append(curr[:])
        left_to_right = not left_to_right
    
    return result
        
#solution
from BinaryTree import *
from TreeNode import *
from collections import deque

def zigzag_level_order(root):
    # If the root is NULL, return an empty list
    if root is None:
        return []

    # Creating an empty list to store the results
    results = []
    # Creating a deque with the root node as the only element
    dq = deque([root])
    # Creating a flag to indicate the direction of the traversal
    reverse = False

    # Traverse the tree
    while len(dq):
        # Getting the size of the current level
        size = len(dq)
        # Insert an empty list at the end of the 'results' list
        results.insert(len(results), [])

        # Traverse the nodes in the current level
        for i in range(size):
            # Check the direction of the traversal
            if not reverse:
                # If the direction is left-to-right, pop a node from the 
                # start (left) of the deque and add it to the current level
                node = dq.popleft()
                results[len(results) - 1].append(node.data)
                # Add the left and right child nodes 
                # of the current node to the deque
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            else:
                # If the direction is right-to-left, pop the a node from the
                # back (right) of the deque and add it to the current level
                node = dq.pop()
                results[len(results) - 1].append(node.data)
                # Add the right and left child nodes 
                # of the current node to the deque
                if node.right:
                    dq.appendleft(node.right)
                if node.left:
                    dq.appendleft(node.left) 

        # Reverse the direction of traversal for the next level
        reverse = not reverse

    # Return the results
    return results

# Driver code
def main():
    # Creating a binary tree
    input1 = [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(350)]
    tree1 = BinaryTree(input1)

    # Creating a right degenerate binary tree
    input2 = [TreeNode(25), TreeNode(50), TreeNode(75), TreeNode(100), TreeNode(200), TreeNode(350)]
    tree2 = BinaryTree(input2)

    # Creating a left degenerate binary tree
    input3 = [TreeNode(350), TreeNode(200), TreeNode(100), TreeNode(75), TreeNode(50), TreeNode(25)]
    tree3 = BinaryTree(input3)

    # Creating a single node binary tree
    tree4 = BinaryTree([TreeNode(100)])

    roots = [tree1.root, tree2.root, tree3.root, tree4.root, None]

    for i in range(len(roots)):
        print(i+1, ".\tBinary Tree:", sep = "")
        display_tree(roots[i])
        print("\n\tThe zigzag level order traversal is:", zigzag_level_order(roots[i]))
        print("\n", "-"*100, "\n", sep = "")

if __name__ == '__main__':
    main()