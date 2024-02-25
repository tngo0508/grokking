# Brute force - backtrack - TLE
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for flight in flights:
            from_i, to_i, price_i = flight
            graph[from_i].append([to_i, price_i])



        def dfs(source, dest, total, num_of_cities, seen):
            if source == dest and num_of_cities - 2 <= k:
                return total

            res = float('inf')
            for nei, price in graph[source]:
                if nei not in seen:
                    seen.add(nei)
                    if num_of_cities - 2 <= k:
                        res = min(res, dfs(nei, dest, total + price, num_of_cities + 1, seen))
                    seen.remove(nei)

            return res

        ans = dfs(src, dst, 0, 1, {src})

        return ans if ans != float('inf') else -1
