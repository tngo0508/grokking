# Brute Force - backtrack - TLE
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        def dfs(idx, curr):

            if idx >= N:
                re = 0
                for subarray in curr:
                    max_val = max(subarray)
                    for _ in range(len(subarray)):
                        re += max_val
                return re

            res = 0
            for i in range(1, k + 1):
                res = max(res, dfs(idx + i, curr + [arr[idx:idx + i]]))
            
            return res

        return dfs(0, [])
    
# Memoization approach - accepted
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        memo = {}

        def dfs(idx):
            if idx in memo:
                return memo[idx]

            if idx >= N:
                return 0

            max_sum = 0
            max_val = 0

            for i in range(1, min(k, N - idx) + 1):
                max_val = max(max_val, arr[idx + i - 1])
                max_sum = max(max_sum, max_val * i + dfs(idx + i))

            memo[idx] = max_sum
            return max_sum

        return dfs(0)