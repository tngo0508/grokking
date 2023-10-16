# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode
from collections import deque

def level_order_traversal(root):
    if not root:
        return "None"

    q = deque([root])
    result = []
    while q:
        n = len(q)
        curr = []
        for _ in range(n):
            node = q.popleft()
            if node:
                curr.append(str(node.data))
            if node:
                q.append(node.left)
                q.append(node.right)
        if curr:
            result.append(curr[:])
    
    return ' : '.join([', '.join(x) for x in result]) if result else "None"

###Solution
# Import required functions
from collections import deque
from BinaryTree import *
from TreeNode import *

# Using two queues
def level_order_traversal(root):
    result = ""
    if not root:
        result = "None"
        return result
    else:
        queues = [deque(), deque()]
        current_queue = queues[0]
        next_queue = queues[1]

        current_queue.append(root)
        level_number = 0
        n = 0

        while current_queue:
            n += 1
            temp = current_queue.popleft()
            result += str(temp.data)

            if temp.left:
                next_queue.append(temp.left)

            if temp.right:
                next_queue.append(temp.right)

            if not current_queue:
                level_number += 1

                if next_queue:
                    result += " : "
                current_queue = queues[level_number % 2]
                next_queue = queues[(level_number + 1) % 2]

            else:
                result += ", "

        return result

# Driver code
def main():
    test_cases_roots = []

    input1 = [
        TreeNode(100),
        TreeNode(50),
        TreeNode(200),
        TreeNode(25),
        TreeNode(75),
        TreeNode(350)
    ]
    tree1 = BinaryTree(input1)
    test_cases_roots.append(tree1.root)

    input2 = [
        TreeNode(25),
        TreeNode(50),
        None,
        TreeNode(100),
        TreeNode(200),
        TreeNode(350)
    ]
    tree2 = BinaryTree(input2)
    test_cases_roots.append(tree2.root)

    input3 = [
        TreeNode(350),
        None,
        TreeNode(100),
        None,
        TreeNode(50),
        TreeNode(25)
    ]
    tree3 = BinaryTree(input3)
    test_cases_roots.append(tree3.root)

    tree4 = BinaryTree([TreeNode(100)])
    test_cases_roots.append(tree4.root)

    test_cases_roots.append(None)

    for i in range(len(test_cases_roots)):
        if i > 0:
            print()
        print(i + 1, ".\tBinary Tree")
        display_tree(test_cases_roots[i])
        print("\n\tLevel order traversal: ")
        print("\t",level_order_traversal(test_cases_roots[i]))
        print("\n" + '-' * 100)


if __name__ == '__main__':
    main()

#### other solution
from collections import deque
from BinaryTree import *
from TreeNode import *


def level_order_traversal(root):
    result = ""
    # Print 'None' if the root is empty
    if not root:
        result = "None"
        return result
    else:
        # Initializing the current queue
        current_queue = deque()

        # Initializing the dummy node
        dummy_node = TreeNode(0)

        current_queue.append(root)
        current_queue.append(dummy_node)

        # Printing nodes in level-order until the current queue remains
        # empty
        while current_queue:
            # Dequeuing and printing the first element of queue
            temp = current_queue.popleft()
            result += str(temp.data)

            # Adding dequeued node's children to the next queue
            if temp.left:
                current_queue.append(temp.left)

            if temp.right:
                current_queue.append(temp.right)

            # When the dummyNode comes next in line, we print a new line and dequeue
            # it from the queue
            if current_queue[0] == dummy_node:
                current_queue.popleft()

                # If the queue is still not empty we add back the dummy node
                if current_queue:
                    result += " : "
                    current_queue.append(dummy_node)
            else:
                result += ", "
        return result


def main():
    test_cases_roots = []

    input1 = [
        TreeNode(100),
        TreeNode(50),
        TreeNode(200),
        TreeNode(25),
        TreeNode(75),
        TreeNode(350)
    ]
    tree1 = BinaryTree(input1)
    test_cases_roots.append(tree1.root)

    input2 = [
        TreeNode(25),
        TreeNode(50),
        None,
        TreeNode(100),
        TreeNode(200),
        TreeNode(350)
    ]
    tree2 = BinaryTree(input2)
    test_cases_roots.append(tree2.root)

    input3 = [
        TreeNode(350),
        None,
        TreeNode(100),
        None,
        TreeNode(50),
        TreeNode(25)
    ]
    tree3 = BinaryTree(input3)
    test_cases_roots.append(tree3.root)

    tree4 = BinaryTree([TreeNode(100)])
    test_cases_roots.append(tree4.root)

    test_cases_roots.append(None)

    for i in range(len(test_cases_roots)):
        if i > 0:
            print()
        print(i + 1, ".\tBinary Tree")
        display_tree(test_cases_roots[i])
        print("\n\tLevel order traversal: ")
        print("\t",level_order_traversal(test_cases_roots[i]))
        print("\n" + '-' * 100)


if __name__ == '__main__':
    main()
