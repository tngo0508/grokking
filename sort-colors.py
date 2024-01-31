class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        RED, WHITE, BLUE = 0, 1, 2
        r, w, b = -1, -1,len(nums)
        i = 0
        while i < len(nums) and i < b:
            if nums[i] == RED:
                r += 1
                nums[i], nums[r] = nums[r], nums[i]
                i += 1
            elif nums[i] == BLUE:
                b -= 1
                nums[i], nums[b] = nums[b], nums[i]
            else:
                w += 1
                i += 1

# Solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag problem solution.
        """
        # For all idx < p0 : nums[idx < p0] = 0
        # curr is an index of elements under consideration
        p0 = curr = 0

        # For all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1