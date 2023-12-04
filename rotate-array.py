class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate_helper(l, r, nums):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        

        rotate_helper(0, len(nums) - 1, nums)
        if k > len(nums):
            k = k % len(nums)
        rotate_helper(0, k - 1, nums)
        rotate_helper(k, len(nums) - 1, nums)