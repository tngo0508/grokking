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
from collections import deque

def can_finish(num_courses, prerequisites):
    counter = 0
    if num_courses <= 0:
        return True

    inDegree = {i: 0 for i in range(num_courses)}
    graph = {i: [] for i in range(num_courses)}

    for edge in prerequisites:
        parent, child = edge[1], edge[0]
        graph[parent].append(child)
        inDegree[child] += 1

    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    while sources:
        course = sources.popleft()
        counter += 1
        for child in graph[course]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    return counter == num_courses
