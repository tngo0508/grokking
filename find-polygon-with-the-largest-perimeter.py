# My solution
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        nums.sort()
        curr_sum = 0 
        ans = -1
        for i, num in enumerate(nums):
            if i >= 2 and curr_sum > num:
                ans = curr_sum + num
            curr_sum += num
    
        return ans