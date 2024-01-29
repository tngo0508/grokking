# use 2 arrays
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [1]
        for num in nums:
            L.append(L[-1] * num)

        R = [1]
        for num in reversed(nums):
            R.append(R[-1] * num)

        R.reverse()

        res = []
        for i in range(len(nums)):
            res.append(L[i] * R[i + 1])
        return res
    
# use 1 array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        products = nums[:]
        for i in range(1, N - 1):
            products[i] = products[i] * products[i - 1]
        
        curr = 1
        for i in reversed(range(N)):
            products[i] = (products[i - 1] if i - 1 >= 0 else 1) * curr 
            curr *= nums[i]
        
        return products