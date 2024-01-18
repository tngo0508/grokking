# Brute Force - TLE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            curr_sum = 0
            for j in range(i, N):
                curr_sum += nums[j]
                if curr_sum == k:
                    res += 1
        return res
    
# Prefix sum approach with Hash map
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = 0
        prefix_sum = 0
        hash_map = defaultdict(int)
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum == k:
                res += 1
            if prefix_sum - k in hash_map:
                res += hash_map[prefix_sum - k]

            hash_map[prefix_sum] += 1

        return res

