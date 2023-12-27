class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, curr, result, nums):
            if len(curr) == len(nums):
                result.append(curr[:])
                return


            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                backtrack(index + 1, curr + [nums[index]], result, nums)
                nums[i], nums[index] = nums[index], nums[i]


        result = []
        backtrack(0, [], result, nums)
        return result