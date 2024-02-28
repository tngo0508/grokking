# DFS - memo - TLE
class Solution:
    def numWays(self, n: int, k: int) -> int:
        memo = defaultdict(tuple)
        def dfs(color, post, curr):
            if len(curr) >= 3 and curr[-1] == curr[-2] and curr[-2] == curr[-3]:
                return 0
            if post == n:
                return 1
            if (color, post, tuple(curr)) in memo:
                return memo[(color, post, tuple(curr))]
            res = 0
            for c in range(k):
                res += dfs(c, post + 1, curr + [c])

            memo[(color, post, tuple(curr))] = res
            return res

        return dfs(0, 0, [])
    
# My solution - DP - accepted
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if k == 0 or n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[1] = k
        for i in range(2, n + 1):
            if i == 2:
                dp[i] = k ** 2
            else:
                dp[i] = (dp[i-1] + dp[i-2]) * (k - 1)
        
        return dp[-1]