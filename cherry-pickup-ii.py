# Memoization Approach
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        memo = defaultdict()
        def dfs(r, r1_c, r2_c):
            if r >= ROWS:
                return 0

            if (r, r1_c, r2_c) in memo:
                return memo[(r, r1_c, r2_c)]

            cols = [-1,0,1]
            res = 0
            for col in cols:
                r1_col = r1_c + col
                if 0 <= r1_col < COLS:
                    for col in cols:
                        r2_col = r2_c + col
                        if 0 <= r2_col < COLS and r1_col != r2_col:
                            res = max(res, dfs(r + 1, r1_col, r2_col) + grid[r][r1_c] + grid[r][r2_c])
                            
            memo[(r, r1_c, r2_c)] = res
            return res

        return dfs(0, 0, COLS - 1)