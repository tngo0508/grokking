from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(queue, heights, visited):
            q = deque(queue)
            while q:
                row, col = q.popleft()
                visited.add((row, col))
                for x, y in [(0,1),(1,0),(0,-1),(-1,0)]:
                    r, c = row + x, col + y
                    if 0 <= r < len(heights) and 0 <= c < len(heights[0]) and (r, c) not in visited:
                        if heights[r][c] >= heights[row][col]:
                            q.append([r, c])

        pacific = []
        atlantic = []
        num_rows = len(heights)
        num_cols = len(heights[0])

        for row in range(num_rows):
            pacific.append([row, 0])
            atlantic.append([row, num_cols-1])
        for col in range(num_cols):
            if [0, col] not in pacific:
                pacific.append([0, col])
            if [num_rows-1, col] not in atlantic:
                atlantic.append([num_rows-1, col])

        p_visited = set()
        a_visited = set()
        result = []
        bfs(pacific, heights, p_visited)
        bfs(atlantic, heights, a_visited)

        for (r, c) in list(a_visited):
            if (r, c) in p_visited:
                result.append([r,c])

        return sorted(result)



