class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums, target):
            res = []
            l, r = 0, len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
            
            return res

        def kSum(nums, target, k):
            output = []
            if not nums:
                return output
            
            avg_val = target // k

            if nums[0] > avg_val or nums[-1] < avg_val:
                return output
            
            if k == 2:
                return twoSum(nums, target)

            for i, num in enumerate(nums):
                if i == 0 or nums[i] != nums[i - 1]:
                    subsets = kSum(nums[i + 1:], target - num, k - 1)
                    for subset in subsets:
                        output.append(subset + [num])
            
            return output


        nums.sort()
        return kSum(nums, target, 4)

# solution


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
	
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            
            # If we have run out of numbers to add, return res.
            if not nums:
                return res
            
            # There are k remaining values to add to the sum. The 
            # average of these values is at least target // k.
            average_value = target // k
            
            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest 
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            
            if k == 2:
                return twoSum(nums, target)
    
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
    
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1
    
            while (lo < hi):
                curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                                                         
            return res

        nums.sort()
        return kSum(nums, target, 4)