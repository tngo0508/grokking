# Memoization - TLE
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        memo = defaultdict()

        def dfs(i):
            if i == N:
                return 0

            if i in memo:
                return memo[i]

            res = 0
            curr_profit = 0
            for j in range(i, N):
                curr_profit = max(curr_profit, prices[j] - prices[i])
                res = max(res, curr_profit + dfs(j + 1))

            memo[i] = res
            return res

        return dfs(0)
    
# Dynamic programming - TLE
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [0] * N
        for i in range(1, N):
            for j in range(i):
                profit = prices[i] - prices[j]
                profit = profit if profit > 0 else 0
                dp[i] = max(dp[i - 1], dp[j] + profit)
        
        return dp[-1]

# My solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        min_so_far = float('inf')
        max_profit = 0
        for i, price in enumerate(prices):
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price, max_profit + price - min_so_far)
            if price - min_price > 0:
                min_so_far = float('inf')
            min_so_far = min(min_so_far, price)
        return max_profit
    
# Editorial solutio
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        # checking if the number current stock is greater than previous, just add the difference
        for i in range(1,len(prices)):
            if (prices[i] > prices[i-1]):
                res += prices[i] - prices[i-1]
        return res