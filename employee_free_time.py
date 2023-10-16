from interval import Interval
import heapq

def employee_free_time(schedule):  
    min_heap = []
    result = []

    for i in range(len(schedule)):
        start = schedule[i][0].start
        end = schedule[i][0].end
        heapq.heappush(min_heap, [[start, end], i, 0])

    prev_interval = min_heap[0][0]
    while min_heap:
        [curr_start, curr_end], employee, idx = heapq.heappop(min_heap)
        if curr_start > prev_interval[1]:
            result.append(Interval(prev_interval[1], curr_start))
        if idx + 1 < len(schedule[employee]):
            next_interval = schedule[employee][idx + 1]
            next_start = next_interval.start
            next_end = next_interval.end
            heapq.heappush(min_heap, [[next_start, next_end], employee, idx + 1])
        prev_interval = [max(prev_interval[0], curr_start), max(prev_interval[1], curr_end)]

    return result