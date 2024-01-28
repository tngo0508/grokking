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