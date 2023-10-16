# Definition of a binary tree node
#
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode

def dfs(node, result):
    if not node:
        result.append('x')
        return
    result.append(str(node.data))
    dfs(node.left, result)
    dfs(node.right, result)

def serialize(root):
    result = []
    dfs(root, result)
    return '*'.join(result)

def construct(stream_list):
    if stream_list[0] == 'x':
        return [None, stream_list]
    root = TreeNode(int(stream_list[0]))
    left, stream_list = construct(stream_list[1:])
    root.left = left
    right, stream_list = construct(stream_list[1:])
    root.right = right

    return [root, stream_list]


def deserialize(stream):
    stream_list = stream.split('*')
    root, _ = construct(stream_list)
    return root

#########
from typing import List, Optional

class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

def serialize_tree(root: Optional[TreeNode]) -> str:
    if not root:
        return 'x'
    return str(root.data) + '*' + serialize_tree(root.left) + '*' + serialize_tree(root.right)

def deserialize_dfs(stream_list: List[str]) -> Tuple[Optional[TreeNode], List[str]]:
    if stream_list[0] == 'x':
        return None, stream_list[1:]
    root = TreeNode(int(stream_list[0]))
    left, stream_list = deserialize_dfs(stream_list[1:])
    root.left = left
    right, stream_list = deserialize_dfs(stream_list)
    root.right = right
    return root, stream_list

def deserialize_tree(stream: str) -> Optional[TreeNode]:
    stream_list = stream.split('*')
    root, _ = deserialize_dfs(stream_list)
    return root

############solution
from BinaryTree import *
from TreeNode import *

# Initializing our marker
MARKER = "M"
m = 1

def serialize_rec(node, stream):
    global m

    if node is None:
        stream.append(MARKER + str(m))
        m += 1
        return

    stream.append(node.data)

    serialize_rec(node.left, stream)
    serialize_rec(node.right, stream)

# Function to serialize tree into list of integers.
def serialize(root):
    stream = []
    serialize_rec(root, stream)
    return stream

def deserialize_helper(stream):
    val = stream.pop()

    if type(val) is str and val[0] == MARKER:
        return None

    node = TreeNode(val)

    node.left = deserialize_helper(stream)
    node.right = deserialize_helper(stream)

    return node

# Function to deserialize integer list into a binary tree.
def deserialize(stream):
    stream.reverse()
    node = deserialize_helper(stream)
    return node

# Driver code
def main():
    global m
    input_trees = [
        [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(350)],
        [TreeNode(100), TreeNode(200), TreeNode(75), TreeNode(50), TreeNode(25), TreeNode(350)],
        [TreeNode(200), TreeNode(350), TreeNode(100), TreeNode(75), TreeNode(50), TreeNode(200), TreeNode(25)],
        [TreeNode(25), TreeNode(50), TreeNode(75), TreeNode(100), TreeNode(200), TreeNode(350)],
        [TreeNode(350), TreeNode(75), TreeNode(25), TreeNode(200), TreeNode(50), TreeNode(100)],
        [TreeNode(1), None, TreeNode(2), None, TreeNode(3), None, TreeNode(4), None, TreeNode(5)]
    ]

    indx = 1
    for i in input_trees:
        tree = BinaryTree(i)

        print(indx, ".\tBinary Tree:", sep="")
        indx += 1
        if tree.root is None:
            display_tree(None)
        else:
            display_tree(tree.root)

        print("\n\tMarker used for NULL nodes in serialization/deserialization: ",
              MARKER, "*", sep="")

        # Serialization
        ostream = serialize(tree.root)
        print("\n\tSerialized integer list:")
        print("\t" + str(ostream))

        # Deserialization
        deserialized_root = deserialize(ostream)
        print("\n\tDeserialized binary tree:")
        display_tree(deserialized_root)
        print("-"*100)
        m = 1

if __name__ == '__main__':
    main()