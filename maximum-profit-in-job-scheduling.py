# Brute Force - TIME LIMIT EXCEEDED
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        temp = []
        N = len(profit)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        @lru_cache(maxsize=None)
        def dfs(index, curr_profit):
            cstart, cend, cprofit = jobs[index]
            curr_profit += cprofit
            dfs.result = max(dfs.result, curr_profit)
            for i in range(index + 1, N):
                nstart, nend, nprofit = jobs[i]
                if nstart >= cend:
                    dfs(i, curr_profit)

        
        dfs.result = 0
        for i in range(len(profit)):
            dfs(i, 0)
        return dfs.result
    
# Optimize solution
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        temp = []
        N = len(profit)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])

        sorted_startTime = [st for st, _, _ in jobs]

        def binary_search_left(sorted_startTime, curr_end):
            left, right = 0, len(sorted_startTime) - 1
            next_index = len(sorted_startTime) # important to avoid the maximum recursion depth
            while left <= right:
                mid = left + (right - left) // 2
                if sorted_startTime[mid] >= curr_end:
                    next_index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            return next_index 
        
        def dfs(index, memo, jobs, sorted_startTime):
            if index == N:
                return 0

            if index in memo:
                return memo[index]

            curr_start, curr_end, curr_profit = jobs[index]

            next_index = binary_search_left(sorted_startTime, curr_end)
            skip = dfs(index + 1, memo, jobs, sorted_startTime)
            take = dfs(next_index, memo, jobs, sorted_startTime) + curr_profit

            max_profit = max(skip, take)
            memo[index] = max_profit
            return max_profit

        
        memo = defaultdict(int)
        return dfs(0, memo, jobs, sorted_startTime)
        