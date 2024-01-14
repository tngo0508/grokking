# Brute Force - TLE
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        N = len(nums)
        def dfs(idx, curr_sum, other_sum):
            if curr_sum == other_sum:
                return True
            for i in range(idx, N):
                if (dfs(i + 1, curr_sum + nums[i], other_sum - nums[i])):
                    return True
            return False

        return dfs(0, 0, total_sum)
    
    
# Memoization - TLE
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        N = len(nums)
        memo = defaultdict()
        def dfs(idx, curr_sum, other_sum):
            if curr_sum == other_sum:
                return True
            
            if (idx, curr_sum, other_sum) in memo:
                return memo[(idx, curr_sum, other_sum)]

            result = False
            for i in range(idx, N):
                result = dfs(i + 1, curr_sum + nums[i], other_sum - nums[i])
                if result:
                    return True

            memo[(idx, curr_sum, other_sum)] = result
            return result

        return dfs(0, 0, total_sum)
    
# other brute force with memo approach - TLE
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        @cache
        def dfs(sum1, sum2, i):
            if i == N:
                print(sum1, sum2)
                return sum1 == sum2
            val = nums[i]
            include = dfs(sum1 + val, sum2, i + 1)
            exclude = dfs(sum1, sum2 + val, i + 1)
            return include or exclude

        return dfs(0, 0, 0)
    
# BFS - TLE
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 1:
            return False

        queue = deque()
        queue.append([nums[0], nums[1]])
        for i in range(2, N):
            next_queue = deque()
            while queue:
                s, t = queue.popleft()
                next_queue.append([s + nums[i], t])
                next_queue.append([s, t + nums[i]])
                next_queue.append([s + t, nums[i]])
            queue = next_queue
        while queue:
            s, t = queue.popleft()
            if s == t:
                return True
        return False


# editorial solution
## Memoization
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(nums: Tuple[int], n: int, subset_sum: int) -> bool:
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
                    or dfs(nums, n - 1, subset_sum))
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(tuple(nums), n - 1, subset_sum)
    
## Dynamic Programming
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        # construct a dp table of size (n+1) x (subset_sum + 1)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[n][subset_sum]