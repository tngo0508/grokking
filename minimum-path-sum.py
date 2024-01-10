# Brute Force - TLE
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(row, col, curr_sum):
            if row == m or col == n:
                return float('inf')

            if row == m - 1 and col == n-1:
                return curr_sum + grid[row][col]

            curr_sum += grid[row][col]
            right = dfs(row, col + 1, curr_sum)
            down = dfs(row + 1, col, curr_sum)
            return min(right, down)

        return dfs(0, 0, 0)

# Memoization - Accepted
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(row, col, memo):
            if row == m or col == n:
                return float('inf')

            if (row, col) in memo:
                return memo[(row, col)]

            if row == m - 1 and col == n-1:
                return grid[row][col]

            right = dfs(row, col + 1, memo) + grid[row][col]
            down = dfs(row + 1, col, memo) + grid[row][col]

            ret_val = min(right, down)
            memo[(row, col)] = ret_val
            return ret_val


        memo = defaultdict()
        return dfs(0, 0, memo)

# Memoization - Table
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        memo = [[-1] * n for _ in range(m)]  # Memoization table

        def dfs(row, col):
            if row == m or col == n:
                return float('inf')

            if row == m - 1 and col == n - 1:
                return grid[row][col]

            if memo[row][col] != -1:
                return memo[row][col]

            right = dfs(row, col + 1)
            down = dfs(row + 1, col)

            # Update memoization table with the minimum path sum for the current cell
            memo[row][col] = grid[row][col] + min(right, down)
            return memo[row][col]

        return dfs(0, 0)
