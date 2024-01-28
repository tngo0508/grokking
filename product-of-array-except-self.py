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