# My solution
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        idx = 0
        N = len(intervals)
        for i in range(N):
            start, end = intervals[i]
            if end < newInterval[0]:
                res.append([start, end])
                idx += 1
            else:
                idx = i
                break

        res.append(newInterval)

        for j in range(idx, N):
            prev_start, prev_end = res[-1]
            start, end = intervals[j]
            if prev_end >= start:
                res[-1][0] = min(prev_start, start)
                res[-1][1] = max(prev_end, end)
            else:
                res.append([start, end])

        return res
