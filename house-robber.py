# Brute Force
class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i, curr):
            if i >= len(nums):
                return curr
            
            rob_curr_house = dfs(i + 2, curr + nums[i])
            rob_next_house = dfs(i + 1, curr)
            return max(rob_curr_house, rob_next_house)

        return dfs(0, 0)
    
# Memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Memoization table
        memo = {}

        def dfs(i, curr):
            if i >= len(nums):
                return curr
            
            # Check if the result for the current subproblem is already computed
            if (i, curr) in memo:
                return memo[(i, curr)]

            rob_curr_house = dfs(i + 2, curr + nums[i])
            rob_next_house = dfs(i + 1, curr)

            # Update memoization table with the result for the current subproblem
            memo[(i, curr)] = max(rob_curr_house, rob_next_house)

            return memo[(i, curr)]

        return dfs(0, 0)

# Dynamic Programming
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]
