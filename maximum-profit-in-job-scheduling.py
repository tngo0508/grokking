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
    
