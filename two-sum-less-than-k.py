class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        l, r = 0, len(sorted_nums) - 1
        result = -1
        while l < r:
            curr_sum = sorted_nums[l] + sorted_nums[r] 
            if curr_sum < k:
                result = max(result, curr_sum)
                l += 1
            else:
                r -= 1
        return result