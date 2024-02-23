# My solution - BFS - Accepted
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for source, destination, price in flights:
            graph[source].append([destination, price])

        queue = deque()
        queue.append([src, 0, 1])
        res = float('inf')
        visit = defaultdict(int)
        visit[src] = 0

        while queue:
            city, total, num_cities = queue.popleft()
            visit[city] = total
            if city == dst and num_cities - 2 <= k:
                res = min(res, total)

            for dest, price in graph[city]:
                if dest in visit and visit[dest] < total + price:
                    continue
                if price > 0 and num_cities + 1 - 2 <= k:
                    queue.append([dest, total + price, num_cities + 1])


        return res if res != float('inf') else -1