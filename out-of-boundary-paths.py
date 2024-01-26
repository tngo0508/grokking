# MEMOIZATION APPROACH - accepted
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        memo = defaultdict()
        def dfs(row, col, move):
            if (row < 0 or row >= m) and move >= 0:
                return 1
            if (col < 0 or col >= n) and move >= 0:
                return 1
            if move <= 0:
                return 0

            if (row, col, move) in memo:
                return memo[(row, col, move)]

            res = 0
            for x, y in ([1,0],[-1,0],[0,1],[0,-1]):
                res += dfs(row + x, col + y, move - 1)

            memo[(row, col, move)] = res % MOD
            return res % MOD

        return dfs(startRow, startColumn, maxMove)