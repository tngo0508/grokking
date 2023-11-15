from collections import deque, defaultdict

def find_order(n, prerequisites):
    in_degree = {i: 0 for i in range(n)}
    graph = defaultdict(list)
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
    
    if len(output) < n:
        return []
    
    return output

# solution
from collections import deque

def find_order(n, prerequisites):
    sorted_order = []
    if n <= 0:
        return sorted_order

    in_degree = {i: 0 for i in range(n)}
    graph = {i: [] for i in range(n)}

    for prerequisite in prerequisites:
        parent, child = prerequisite[1], prerequisite[0]
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    if len(sorted_order) != n:
        return []

    return sorted_order


# Driver code
def main():
    n = [4, 5, 0, 4, 7]
    prerequisites = [
      [[1, 0], [2, 0], [3, 1], [3, 2]], 
      [[1, 0], [2, 0], [3, 1], [4, 3]], 
      [[1, 0]], [[1, 0], [2, 0], [3, 1], [3, 2]], 
      [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]]
    for i in range(len(n)):
        print(i + 1, ".\tPrerequisites: ", prerequisites[i], sep="")
        print("\tTotal number of courses, n:", n[i])
        print("\tValid courses order:", find_order(n[i], prerequisites[i]))
        print("-"*100)


if __name__ == '__main__':
    main()
