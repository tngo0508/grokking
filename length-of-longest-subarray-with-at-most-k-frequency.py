# My solution - sliding window - accepted
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        start = end = 0
        freq = defaultdict(int)
        res = 0
        for end, num in enumerate(nums):
            freq[num] += 1
            while start <= end and freq[num] > k:
                freq[nums[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        
        return res