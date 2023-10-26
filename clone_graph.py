from Node import *
from collections import defaultdict

def dfs(root, hash_map):
    if not root:
        return

    newRoot = Node(root.data)
    hash_map[root] = newRoot
    for nei in root.neighbors:
        if nei in hash_map:
            newRoot.neighbors.append(hash_map[nei])
        elif nei not in newRoot.neighbors:
            newRoot.neighbors.append(dfs(nei, hash_map))
    
    return newRoot


def clone(root):
    if not root:
        return
    hash_map = defaultdict(Node)
    dfs(root, hash_map)
    return hash_map[root]

# solution
from graph_utility import *

def clone_helper(root, nodes_completed):
    if root == None:
      return None

    cloned_node = Node(root.data)
    nodes_completed[root] = cloned_node

    for p in root.neighbors:
      x = nodes_completed.get(p)
      if not x:
        cloned_node.neighbors += [clone_helper(p, nodes_completed)]
      else:
        cloned_node.neighbors += [x]
    return cloned_node

def clone(root):
    nodes_completed = {}
    return clone_helper(root, nodes_completed)

# Driver code
def main():
    data = [[[2, 3], [1, 3], [1, 2]],
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            [[2, 5], [1, 3], [2, 4], [3, 5], [1, 4]],
            [[2], [1]],
            [[2, 6], [1, 3], [2, 4], [3, 5], [4, 6], [1, 5]],
            [[]]
            ]

    for i in range (len(data)):
      node1 = create_graph(data[i])
      print(i+1, ".\t Original Graph: ", create_2D_list(node1), "\n", sep="")
      print_graph(node1)
      print()
      cloned_root = clone(node1)
      print("\t Cloned Graph: ", create_2D_list(cloned_root), "\n", sep="")
      print_graph(node1)
      print("-"*100)  

main()