# Brute Force - TLE
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        def generate_permutation(idx, nums, perms):
            if idx == n:
                perms.append(nums[:])
                return
            for i in range(idx, n):
                nums[i], nums[idx] = nums[idx], nums[i]
                generate_permutation(idx + 1, nums, perms)
                nums[i], nums[idx] = nums[idx], nums[i]

        nums = [i for i in range(1, n + 1)]
        perms = []
        generate_permutation(0, nums, perms)
        res = 0
        for perm in perms:
            count = 0
            for i in range(n):
                for j in range(i + 1, n):
                    if perm[i] > perm[j]:
                        count += 1
        
            if count == k:
                res += 1
        
        return res
    
# Better Brute Foruce - TLE
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        def dfs(max_num, pairs):
            if pairs < 0:
                return 0
            if max_num == 0:
                return pairs == 0
            res = 0
            for i in range(max_num):
                res = (res + dfs(max_num - 1, pairs - i)) % MOD

            return res

        return dfs(n, k)
    
# Memoization
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(max_num, pairs):
            if pairs < 0:
                return 0
            if max_num == 0:
                return pairs == 0
            res = 0
            for i in range(min(pairs + 1, max_num)):
                res = (res + dfs(max_num - 1, pairs - i)) % MOD

            return res

        return dfs(n, k)