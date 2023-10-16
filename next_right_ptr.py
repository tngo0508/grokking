from EduBinaryTree import *
from EduTreeNode import *

def populate_next_pointers(root):
    if not root:
        return root

    mostleft = root 

    while mostleft.left:

        current = mostleft

        while current:

            current.left.next = current.right

            if current.next:
                
                current.right.next = current.next.left

            current = current.next

        mostleft = mostleft.left

    return root

# Driver code
def main():
    input = [EduTreeNode(100), EduTreeNode(50), EduTreeNode(200), EduTreeNode(25), EduTreeNode(75), EduTreeNode(300), EduTreeNode(10)]
    tree = EduBinaryTree(input)

    populate_next_pointers(tree.root)
    index_val = 0
    print("Binary tree:")
    display_tree(tree.root)
    print()
    for node_value in input:
        index_val += 1
        tmp = EduBinaryTree.get_next_node(tree.root, node_value.data)
        sib_node = "None"
        if (tmp != None):
            sib_node = str(tmp.data)
        print(index_val, ".", sep="", end="")
        print("\tCurrent Node Value: ", node_value.data, sep="")
        print("\tNext Node Value: ", sib_node, sep="")
        print("-"*100, "\n", sep="")


if __name__ == '__main__':
    main()