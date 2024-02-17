# My solution
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        required_bricks = [] # min heap
        for i in range(N - 1):
            if heights[i] < heights[i + 1]:
                difference = heights[i + 1] - heights[i]
                
                if ladders > 0:
                    ladders -= 1
                    heapq.heappush(required_bricks, difference)
                else:
                    if required_bricks and required_bricks[0] < difference:
                        min_height = heapq.heappop(required_bricks)
                        bricks -= min_height
                        heapq.heappush(required_bricks, difference)
                    else:
                        bricks -= difference
                
                if ladders <= 0 and bricks < 0:
                    return i

        return N - 1