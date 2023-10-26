from collections import deque
from queue import PriorityQueue

def network_delay_time(times, n, k):
    graph = {i + 1: [] for i in range(n)}
    for src, dst, w in times:
        graph[src].append([dst, w])
    
    q = PriorityQueue()
    q.put([0, k])
    res = -1
    visit = set()
    while not q.empty():
        delay, node = q.get()
        if node in visit:
            continue
        visit.add(node)
        res = max(res, delay)

        for nei in graph[node]:
            next_node, w = nei
            if next_node not in visit:
                q.put([delay + w, next_node])
    
    return res if len(visit) == n else -1