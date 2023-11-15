from collections import deque, defaultdict
def can_finish(num_courses, prerequisites):
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(num_courses)}
    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1
    
    queue = deque()
    for k, v in in_degree.items():
        if v == 0:
            queue.append(k)
    
    output = []
    while queue:
        node = queue.popleft()
        output.append(node)
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)
    
    return len(output) == num_courses

# SOLUTION
from collections import deque, defaultdict
def can_finish(num_courses, prerequisites):
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(num_courses)}
    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1
    
    queue = deque()
    for k, v in in_degree.items():
        if v == 0:
            queue.append(k)
    
    output = []
    while queue:
        node = queue.popleft()
        output.append(node)
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)
    
    return len(output) == num_courses
