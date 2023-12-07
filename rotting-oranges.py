from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
      q = deque()
      n = len(grid)
      m = len(grid[0])
      fresh_oranges = 0
      for r in range(n):
        for c in range(m):
          if grid[r][c] == 2:
            q.append([r, c, 0])
          if grid[r][c] == 1:
            fresh_oranges += 1
      
      minute = 0
      while q:
        x, y, minute = q.popleft()
        
        for row, col in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
          if 0 <= row < n and 0 <= col < m and grid[row][col] == 1:
            q.append([row, col, minute + 1])
            fresh_oranges -= 1
            grid[row][col] = 2
      

      return minute if fresh_oranges == 0 else -1
    
# solution
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Step 1). build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Mark the round / level, _i.e_ the ticker of timestamp
        queue.append((-1, -1))

        # Step 2). start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # We finish one round of processing
                minutes_elapsed += 1
                if queue:  # to avoid the endless loop
                    queue.append((-1, -1))
            else:
                # this is a rotten orange
                # then it would contaminate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))

        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1