from interval import *

def insert_interval(existing_intervals, new_interval):
    if not existing_intervals:
        return []
    
    sorted_existing_intervals = sorted(existing_intervals, key=lambda x: x.start)
    result = [sorted_existing_intervals[0]]
    idx = 1
    for i in range(1, len(sorted_existing_intervals)):
        current_start = sorted_existing_intervals[i].start
        current_end = sorted_existing_intervals[i].end
        current_interval = Interval(current_start, current_end)

        idx = i
        if result[-1].end >= new_interval.start:
            break

        if current_start <= result[-1].end:
            result[-1].end = max(current_end, result[-1].end)
        else:
            result.append(current_interval)


    if new_interval.start <= result[-1].end:
        result[-1].end = max(result[-1].end, new_interval.end)
    else:
        result.append(new_interval)

    for i in range(idx, len(sorted_existing_intervals)):
        current_start = sorted_existing_intervals[i].start
        current_end = sorted_existing_intervals[i].end
        current_interval = Interval(current_start, current_end)
        if current_start <= result[-1].end:
            result[-1].end = max(current_end, result[-1].end)
        else:
            result.append(current_interval)
    return result

#####################################################################
from typing import List
from interval import Interval

def insert_interval(existing_intervals: List[Interval], new_interval: Interval) -> List[Interval]:
    if not existing_intervals:
        return []

    result = []
    interval_index = 0

    while interval_index < len(existing_intervals) and existing_intervals[interval_index].end < new_interval.start:
        result.append(existing_intervals[interval_index])
        interval_index += 1

    while interval_index < len(existing_intervals) and existing_intervals[interval_index].start <= new_interval.end:
        new_interval.start = min(new_interval.start, existing_intervals[interval_index].start)
        new_interval.end = max(new_interval.end, existing_intervals[interval_index].end)
        interval_index += 1

    result.append(new_interval)

    while interval_index < len(existing_intervals):
        result.append(existing_intervals[interval_index])
        interval_index += 1

    return result