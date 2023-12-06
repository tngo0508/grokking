from collections import defaultdict
from typing import List
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def dfs(graph, node, quiet, visited):
            if quiet[node] <= quiet[dfs.ans]:
                dfs.ans = node
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(graph, nei, quiet, visited)

        graph = defaultdict(list)
        for src, dst in richer:
            graph[dst].append(src)
        
        result = []
        n = len(quiet)
        for i in range(n):
            visited = set()
            dfs.ans = i
            dfs(graph, i, quiet, visited)
            result.append(dfs.ans)

        return result

# leetcode solution
class Solution(object):
    def loudAndRich(self, richer, quiet):
        N = len(quiet)
        graph = [[] for _ in xrange(N)]
        for u, v in richer:
            graph[v].append(u)

        answer = [None] * N
        def dfs(node):
            #Want least quiet person in this subtree
            if answer[node] is None:
                answer[node] = node
                for child in graph[node]:
                    cand = dfs(child)
                    if quiet[cand] < quiet[answer[node]]:
                        answer[node] = cand
            return answer[node]

        return map(dfs, range(N))