class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        for i in range(1, N):
            j = i - 1
            while j >= 0:
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                j -= 1
        
        return max(dp)
