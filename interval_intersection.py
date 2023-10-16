from interval import Interval

def intervals_intersection(interval_list_a, interval_list_b):
    idx_a = 0
    idx_b = 0
    result = []
    while idx_a < len(interval_list_a) and idx_b < len(interval_list_b):
        start_a, end_a = interval_list_a[idx_a].start, interval_list_a[idx_a].end
        start_b, end_b = interval_list_b[idx_b].start, interval_list_b[idx_b].end

        if end_a < start_b:
            idx_a += 1
            continue
        if end_b < start_a:
            idx_b += 1
            continue

        if start_a <= end_b or start_b <= end_a:
            result.append(Interval(max(start_a, start_b), min(end_a, end_b)))
        
        if end_a < end_b:
            idx_a += 1
        elif end_b < end_a:
            idx_b += 1
        else:
            idx_a += 1
            idx_b += 1
    
    return result