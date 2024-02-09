# Brute Force - TLE
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        def is_valid(arr):
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    if arr[i] % arr[j] != 0:
                        return False
            return True

        N = len(nums)
        nums.sort(reverse=True)
        def dfs(idx, curr):
            if idx == N:
                if is_valid(curr):
                    return curr[:]
                return []
            res = []
            for i in range(idx, N):
                exclude = dfs(i + 1, curr)
                include = dfs(i + 1, curr + [nums[i]])
                if len(res) < len(exclude):
                    res = exclude[:]
                if len(res) < len(include):
                    res = include[:]
            
            return res

        return dfs(0, [])

# Memoization - MLE
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        def is_valid(arr):
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    if arr[i] % arr[j] != 0:
                        return False
            return True

        N = len(nums)
        nums.sort(reverse=True)
        @cache
        def dfs(idx, curr):
            curr = list(curr)
            if idx == N:
                if is_valid(curr):
                    return tuple(curr[:])
                return []
            res = []
            for i in range(idx, N):
                exclude = dfs(i + 1, tuple(curr))
                include = dfs(i + 1, tuple(curr + [nums[i]]))
                if len(res) < len(exclude):
                    res = exclude[:]
                if len(res) < len(include):
                    res = include[:]
            
            return res

        return dfs(0, tuple())


