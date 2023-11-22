from collections import defaultdict
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)

        def backtrack(node, target, acc_product, visited):
            visited.add(node)
            res = -1
            if target in graph[node]:
                res =  acc_product * graph[node][target]
            else:
                for nei, val in graph[node].items():
                    if nei in visited:
                        continue
                    res = backtrack(nei, target, acc_product * val, visited)
                    if res != -1:
                        break
            visited.remove(node)
            return res
        
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        result = []
        for dividend, divisor in queries:
            res = 0
            if dividend not in graph or divisor not in graph:
                res = -1
            elif dividend == divisor:
                res = 1
            else:
                visited = set()
                res = backtrack(dividend, divisor, 1, visited)

            result.append(res)
        
        
        return result