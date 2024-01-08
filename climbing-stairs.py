# brute force - memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i, memo):
            if i > n:
                return 0

            if i == n:
                return 1
            
            if i in memo:
                return memo[i]
            
            one_step = dfs(i + 1, memo)
            two_step = dfs(i + 2, memo)
            memo[i] = one_step + two_step
            return memo[i]

        memo = defaultdict(int)
        return dfs(0, memo)
    
# Dynamic Programming
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        dp = [0] * (n + 1)
        dp[1] = dp[0] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]