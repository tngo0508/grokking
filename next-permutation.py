class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        end  = N - 1
        while end > 0 and nums[end] <= nums[end - 1]:
            end -= 1
        
        start = end
        while start < N and nums[start] > nums[end - 1]:
            start += 1
        
        nums[start - 1], nums[end - 1] = nums[end - 1], nums[start - 1]
        nums[end:] = sorted(nums[end:])

        