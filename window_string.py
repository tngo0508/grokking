from collections import defaultdict
from collections import Counter
import sys

# def is_valid(window_dict, t_dict):
#     for c, count in t_dict.items():
#         if window_dict[c] < count:
#             return False
#     return True

def is_valid(window_dict, t_dict):
    return all(window_dict[c] >= count for c, count in t_dict.items())

def min_window(s, t):
    if len(t) == 0:
        return ""
    freq_t = Counter(t)
    freq_window = defaultdict(int)
    start, end = 0, 0
    # min_length = float('inf')
    min_length = sys.maxsize
    result = ""
    for end, c in enumerate(s):
        freq_window[c] += 1
        if len(freq_window) < len(freq_t):
            continue
        while is_valid(freq_window, freq_t) and start <= end:
            if min_length > end - start + 1:
                min_length = end - start + 1
                result = s[start:end + 1]

            freq_window[s[start]] -= 1
            start += 1
    
    return result

print(min_window("ABCD", "ABC"))
print(min_window("XYZYX", "XYZ"))
print(min_window("ABXYZJKLSNFC", "ABC"))
print(min_window("AAAAAAAA", "A"))