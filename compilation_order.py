from graph import *
from collections import deque, defaultdict

def find_compilation_order(dependencies):
  graph = defaultdict(list)
  in_degree = defaultdict(int)
  queue = deque()
  sorted_order = []
  classes = set()

  for des, src in dependencies:
    graph[src].append(des)
    in_degree[des] += 1
    classes.add(des)
    classes.add(src)

  for x in list(classes):
    if x not in in_degree:
      queue.append(x)
  
  while queue:
    node = queue.popleft()
    sorted_order.append(node)
    if node in graph:
      for nei in graph[node]:
        in_degree[nei] -= 1
        if in_degree[nei] == 0:
          queue.append(nei)
          
  # topological sort is not possible as the graph has a cycle
  if len(sorted_order) != len(graph):
    return []
  return sorted_order

# solution
from collections import deque


def find_compilation_order(dependencies):
    sorted_order = []
    graph = {}
    inDegree = {}
    for x in dependencies:
        parent, child = x[1], x[0]
        graph[parent], graph[child] = [], []
        inDegree[parent], inDegree[child] = 0, 0
    if len(graph) <= 0:
        return sorted_order


    for dependency in dependencies:
        parent, child = dependency[1], dependency[0]
        graph[parent].append(child)  
        inDegree[child] += 1  

    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]: 
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sorted_order) != len(graph):
        return []
    return sorted_order
  
  
  

