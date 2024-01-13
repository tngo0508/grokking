# Brute force
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        res = float('-inf')
        for i in range(N):
            res = max(res, nums[i])
            curr_product = nums[i]
            for j in range(i + 1, N):
                curr_product *= nums[j]
                res = max(res, curr_product)
        
        return res
    
# dynamic programming
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxproduct,minproduct,result=nums[0],nums[0],nums[0]
        for i in nums[1:]:
            temp=[i,i*maxproduct,i*minproduct]
            maxproduct=max(temp)
            minproduct=min(temp)

            result=max(result,maxproduct)
        return result
            
# editorial solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result