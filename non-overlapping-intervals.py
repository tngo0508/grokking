class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        result = 0
        merge = [intervals[0]]
        for interval in intervals[1:]:
            _, end = merge[-1]
            curr_start, curr_end = interval
            if curr_start < end:
                result += 1
                merge[-1][1] = min(end, curr_end)
            else:
                merge.append(interval[:])
        
        return result

# solution
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        ans = 0
        k = -inf
        
        for x, y in intervals:
            if x >= k:
                # Case 1
                k = y
            else:
                # Case 2
                ans += 1
        
        return ans