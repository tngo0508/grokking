# Brute force - TLE
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        res = []
        for end in range(len(nums)):
            if end - start + 1 == k:
                res.append(max(nums[start:end+1]))
                start += 1
        return res