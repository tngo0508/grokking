# My solution
from heapq import *
class MedianFinder:

    def __init__(self):
        self.min_heap = [] # larger numbers
        self.max_heap = [] # smaller numbers
        

    def addNum(self, num: int) -> None:
        if not self.max_heap and not self.min_heap:
            heappush(self.max_heap, -num)
            return

        if self.max_heap and num > -self.max_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)
        
        if len(self.max_heap) - len(self.min_heap) >= 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        
        if len(self.min_heap) - len(self.max_heap) >= 2:
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        # print(f'smaller: {self.max_heap}')
        # print(f'larger: {self.min_heap}')
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        return self.min_heap[0] if self.min_heap else -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
    
