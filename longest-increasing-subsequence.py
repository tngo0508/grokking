# Brute force - TLE
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        result = 0

        def dfs(index, curr_num):
            if index == N:
                return 0

            max_length = 0
            for i in range(index + 1, N):
                if curr_num < nums[i]:
                    length = dfs(i, nums[i]) + 1
                    max_length = max(max_length, length)

            return max_length
        
        
        for i in range(N):
            result = max(result, dfs(i, nums[i]) + 1)
        return result
    
# Memoization - Accepted
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        result = 0
        memo = defaultdict()

        def dfs(index, curr_num):
            if index == N:
                return 0

            if (index, curr_num) in memo:
                return memo[(index, curr_num)]

            max_length = 0
            for i in range(index + 1, N):
                if curr_num < nums[i]:
                    length = dfs(i, nums[i]) + 1
                    max_length = max(max_length, length)

            memo[(index, curr_num)] = max_length
            return max_length
        
        
        for i in range(N):
            result = max(result, dfs(i, nums[i]) + 1)
        return result

# Dynamic programming
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
    

