class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + num < 0:
                    l += 1
                elif nums[l] + nums[r] + num > 0:
                    r -= 1
                else:
                    arr = [num, nums[l], nums[r]]
                    if arr not in result:
                        result.append(arr[:])
                    l += 1
                    r -= 1
        return result
                
