class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for index , height in enumerate(heights):
            start = index
            
            while start and stack[-1][1] > height:
                i , h = stack.pop()
                maxArea = max(maxArea , (index-i)*h)
                start = i
            stack.append((start , height))

        for index , height in stack:
            maxArea = max(maxArea , (len(heights)-index)*height)

        return maxArea    

                


# other solution
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        stk = [-1]
        res = 0
        for ind, h in enumerate(heights):
            while h < heights[stk[-1]]:
                cur_h = heights[stk.pop()]
                width = ind - 1 - stk[-1]
                res = max(res, cur_h * width)
            stk.append(ind)
        return res