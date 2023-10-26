def valid_tree(n, edges):
    if len(edges) != n - 1:
        return False
    
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for x, y in edges:
        graph[x][y] = 1

    visited = set()
    stack = [0]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for i in range(n):
            if graph[node][i] == 1:
                stack.append(i)

    return len(visited) == n

    
# solution
def valid_tree(n, edges):
    if (len(edges) != (n - 1)):
      return False

    adjacency = []
    for i in range(n):
        adjacency.append([])
        
    for x, y in edges:
        adjacency[x].append(y)
        adjacency[y].append(x)

    visited = {0}
    stack = [0]

    while stack:
        node = stack.pop()
        for neighbor in adjacency[node]:
            if neighbor in visited:
                continue

            visited.add(neighbor)
            stack.append(neighbor)

    if len(visited) == n:
        return True

    return False


# Driver code
def main():
    n = [3, 4, 5, 5, 6]
    edges = [
                [[0, 1], [0, 2], [1, 2]], 
                [[0, 1], [0, 2], [0, 3]], 
                [[0, 1], [0, 2], [0, 3], [0, 4], [3, 4]], 
                [[0, 1], [0, 2], [0, 3], [3, 4]], 
                [[0, 1], [0, 2], [1, 3], [2, 4], [0, 5]]
            ]

    for i in range(len(n)):
        print(i + 1, ".\t n = ", n[i], sep="")
        print("\t Edges = ", edges[i], sep="")
        print("\t Is the given graph a valid tree:", valid_tree(n[i], edges[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()