from heapq import *
from min_heap import *
from max_heap import *


def maximum_capital(c, k, capitals, profits):
    min_heap = []
    max_heap = []
    for i, capital in enumerate(capitals):
        heappush(min_heap, [capital, i])
    
    while k > 0:
        while min_heap and min_heap[0][0] <= c:
            capital, i = heappop(min_heap)
            heappush(max_heap, [-profits[i], i])
        
        if not max_heap:
            break
        profit, i = heappop(max_heap)
        c += -profit
        k -= 1
        

    return c