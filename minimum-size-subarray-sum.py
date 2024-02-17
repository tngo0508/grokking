# My solution - sliding window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        N = len(nums)
        curr_sum = 0
        res = float('inf')
        for end in range(N):
            curr_sum += nums[end]
            while start <= end and curr_sum >= target:
                if curr_sum >= target:
                    res = min(res, end - start + 1)
                curr_sum -= nums[start]
                start += 1
        
        return res if res != float('inf') else 0