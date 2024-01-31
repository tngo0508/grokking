class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        if 1 not in nums:
            return 1
        
        for i in range(N):
            if nums[i] <= 0 or nums[i] > N:
                nums[i] = 1
        
        for i in range(N):
            val = abs(nums[i])
            if val == N:
                nums[0] = -abs(nums[0])
            else:
                nums[val] = -abs(nums[val])
        
        for i in range(1, N):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return N
        
        return N + 1
