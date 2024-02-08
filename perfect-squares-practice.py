# Memoization - TLE
class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        for i in range(1, n + 1):
            square = i**2
            if square <= n:
                nums.append(square)
            else:
                break
        
        nums.sort(reverse=True)
        memo = defaultdict()
        
        def dfs(i, n):
            if n < 0:
                return float('inf')
            if n == 0:
                return 0
            if (i, n) in memo:
                return memo[(i, n)]
            res = float('inf')
            for j in range(i, len(nums)):
                res = min(res, dfs(j, n - nums[j]) + 1, dfs(j + 1, n) + 1)
            
            memo[(i, n)] = res
            return res

        return dfs(0, n)
    
# Dynamic programing - TLE
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        for i in range(n + 1):
            if i ** 2 > n:
                break
            dp[i**2] = 1
        
        for i in range(1, n + 1):
            for j in range(0, i//2 + 1):
                dp[i] = min(dp[i], dp[i - j] + dp[j])
        
        return dp[-1]
    
# BFS - memory limit exceeded
class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        for i in range(n + 1):
            if i ** 2 > n:
                break
            nums.append(i**2)

        nums.sort(reverse=True)
        queue = deque()
        queue.append([n, 0])
        while queue:
            total, level = queue.popleft()
            if total < 0:
                continue
            if total == 0:
                return level
            
            for num in nums:
                queue.append([total - num, level + 1])
        
        return res
    
# Improved BFS - Accepted
class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        for i in range(n + 1):
            if i ** 2 > n:
                break
            nums.append(i**2)

        queue = deque()
        queue.append([n, 0])
        while queue:
            total, level = queue.popleft()
            for num in nums:
                if total - num == 0:
                    return level + 1
                if total - num < 0:
                    continue
                queue.append([total - num, level + 1])
        
        return res

