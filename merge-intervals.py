class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            _, prev_end = res[-1]
            if start <= prev_end:
                res[-1][1] = max(end, prev_end)
            else:
                res.append([start, end])
        
        return res