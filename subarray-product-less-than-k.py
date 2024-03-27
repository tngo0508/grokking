class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        start = end = 0
        curr = 1
        res = 0
        while end < N:
            curr *= nums[end]
            while start <= end and curr >= k:
                curr //= nums[start] 
                start += 1
            res += end - start + 1
            end += 1
        
        return res