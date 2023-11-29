class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]

        while l <= r:
            m = l + (r - l) // 2
            print(f'l: {l}, m: {m}, r: {r}')
            if m - 1 >= 0 and m + 1 < len(nums) and nums[m - 1] > nums[m] and nums[m + 1] > nums[m]:
                return nums[m]
            else:
                if nums[m] < nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return nums[r]