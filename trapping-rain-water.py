# Brute force - TLE
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(1, len(height)):
            l = r = 0
            for j in range(i, -1, -1):
                l = max(l, height[j])
            for j in range(i, len(height)):
                r = max(r, height[j])
            res += min(l, r) - height[i]
        return res
    
# Dynamic Programming 1D - Accepted - left right approach
class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        curr_max = 0
        water = [0] * len(height)
        for i in range(N):
            curr_max = max(curr_max, height[i])
            water[i] = curr_max - height[i]
        
        curr_max = 0
        for j in reversed(range(N)):
            curr_max = max(curr_max, height[j])
            water[j] = min(water[j], curr_max - height[j])
        
        return sum(water)
    
# two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r = 0,len(height)-1
        ans = 0
        leftmx, rightmx = 0,0

        while l<r:
            if height[l]<height[r]:
                if height[l]>leftmx:
                    leftmx= height[l]
                else:
                    ans+= (leftmx-height[l])
                l+=1
            else:
                if height[r]>rightmx:
                    rightmx= height[r]
                else:
                    ans+= (rightmx-height[r])
                r-=1

        return ans
    
# Monotonic decreasing stack
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for end, curr_height in enumerate(height):
            while stack and height[stack[-1]] < curr_height:
                j = stack.pop()
                if stack:
                    start = stack[-1]
                    height_start = height[start]
                    h = min(curr_height, height_start) - height[j]
                    d = end - start - 1
                    water += (d * h)
            stack.append(end)
        return water