# Brute Force
class Solution:
    def numSquares(self, n: int) -> int:
        def dfs(num, curr_sum):
            if curr_sum == 0:
                return 0

            if curr_sum < 0:
                return float('inf')

            result = float('inf')
            for x in range(1, curr_sum + 1):
                square = x **2
                result = min(result, dfs(x, curr_sum - square) + 1)

            return result

        return dfs(0, n)