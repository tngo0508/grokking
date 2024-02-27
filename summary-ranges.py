# My solution
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        N = len(nums)
        start = 0
        end = 1
        for end in range(1, N):
            if nums[end] != nums[end - 1] + 1:
                if start != end - 1:
                    res.append(str(nums[start]) + "->" + str(nums[end - 1]))
                else:
                    res.append(str(nums[start]))
                start = end

        if start != end and end < len(nums):
            res.append(str(nums[start]) + "->" + str(nums[end]))
        else:
            res.append(str(nums[start]))
        return res

# Editorial solution


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        i = 0

        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1

            if start != nums[i]:
                ranges.append(str(start) + "->" + str(nums[i]))
            else:
                ranges.append(str(nums[i]))

            i += 1

        return ranges
