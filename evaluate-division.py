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
    

    def union_find_solution(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        gid_weight = {}

        def find(node_id):
            group_id, node_weight = gid_weight.setdefault(node_id, (node_id, 1))

            if group_id != node_id:
                new_group_id, group_weight = find(group_id)
                gid_weight[node_id] = (new_group_id, node_weight * group_weight)
            
            return gid_weight[node_id]

        def union(dividend, divisor, value):
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                '''
                for someone who don't understand divisorWeight * value / dividendWeight in the Union Find solution
                dividend / dividend_root = dividendWeight
                divisor / divisor_root = divisorWeight
                dividend / divisor = value
                after union, divisor_root becomes root of dividend_root
                --> (divisor / divisor_root) / (dividend / dividend_root) = divisorWeight / dividendWeight
                --> dividend_root / divisor_root = divisorWeight * value / dividendWeight
                '''
                gid_weight[dividend_gid] = (divisor_gid, divisor_weight * value / dividend_weight)
            
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)

        results = []
        for (dividend, divisor) in queries:
            if dividend not in gid_weight or divisor not in gid_weight:
                results.append(-1.0)
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                    results.append(-1.0)
                else:
                    results.append(dividend_weight / dividend_weight)
        
        return results
            
        