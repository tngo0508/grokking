class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                res.append(num)
            seen.add(num)
        for i in range(1, len(nums) + 1):
            if i not in seen:
                res.append(i)
                break
        return res

            