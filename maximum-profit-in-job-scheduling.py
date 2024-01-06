# Brute Force - TIME LIMIT EXCEEDED
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        temp = []
        N = len(profit)
        for i in range(N):
            start = startTime[i]
            end = endTime[i]
            p = profit[i]
            temp.append([start, end, p])
        temp.sort()

        sorted_startTime = []
        sorted_endTime = []
        sorted_profit = []
        for i in range(N):
            sorted_startTime.append(temp[i][0])
            sorted_endTime.append(temp[i][1])
            sorted_profit.append(temp[i][2])
        
        @lru_cache(maxsize=None)
        def dfs(index, curr_profit):
            curr_profit += sorted_profit[index]
            dfs.result = max(dfs.result, curr_profit)
            for i in range(index + 1, N):
                curr_end = sorted_endTime[index]
                next_start = sorted_startTime[i]
                if next_start >= curr_end:
                    dfs(i, curr_profit)

        
        dfs.result = 0
        for i in range(len(profit)):
            dfs(i, 0)
        return dfs.result