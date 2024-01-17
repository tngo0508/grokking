class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        seen = set()
        res = 0
        for num in nums:
            if num not in seen:
                lo, hi = num, num
                while num + 1 in set_nums:
                    hi = num + 1
                    num += 1
                    seen.add(hi)
                while num - 1 in set_nums:
                    lo = num - 1
                    num -= 1
                    seen.add(lo)
                res = max(res, hi - lo + 1)
                seen.add(num)
        return res
        