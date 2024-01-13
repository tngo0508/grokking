# Brute Force - TLE
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
    
# Memoization - TLE
import math
class Solution:
    def numSquares(self, n: int) -> int:
        memo = defaultdict()
        def dfs(curr_sum):
            if curr_sum == 0:
                return 0

            if curr_sum < 0:
                return float('inf')

            if curr_sum in memo:
                return memo[curr_sum]

            result = float('inf')
            for x in range(1, math.ceil(curr_sum / 2) + 1):
                square = x **2
                result = min(result, dfs(curr_sum - square) + 1)

            memo[curr_sum] = result
            return result

        return dfs(n)
    
# Dynamic Programming - Bottom-up Approach
import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        x = 1
        while x ** 2 <= n:
            dp[x**2] = 1
            x += 1
        
        closest_square = [1]
        for i in range(1, n + 1):
            if dp[i] == 1:
                closest_square.append(i)
            else:
                for square in closest_square:
                    dp[i] = min(dp[i], dp[i - square] + dp[square])

        return dp[-1]

# Editorial Solution
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        
        dp = [float('inf')] * (n+1)
        # bottom case
        dp[0] = 0
        
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        
        return dp[-1]