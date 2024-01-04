class Solution:
    def minOperations(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def helper(n):
            if n < 0:
                return float('inf')
            if n == 0:
                return 0
            
            first = helper(n - 3) + 1
            second = helper(n - 2) + 1
            return min(first, second)

        counter = Counter(nums)
        result = 0
        for v in counter.values():
            val = helper(v)
            if val == float('inf'):
                return -1
            result += helper(v)
        return result
    
# Leet Code Solution
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            if c == 1: 
                return -1
            ans += ceil(c / 3)
        return ans