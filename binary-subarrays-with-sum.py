# Brute Force - TLE
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            curr_sum = 0
            for j in range(i, N):
                curr_sum += nums[j]
                if curr_sum == goal:
                    res += 1
        
        return res

# Prefix sum - hash map approach
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        N = len(nums)
        res = 0
        curr_sum = 0
        prefix_sum = defaultdict(int)
        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum == goal:
                res += 1
            if curr_sum - goal in prefix_sum:
                res += prefix_sum[curr_sum - goal]
            prefix_sum[curr_sum] += 1
        
        return res