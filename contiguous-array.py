# Brute Force - TLE
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        N = len(nums)
        max_length = 0
        for i in range(N):
            counter = Counter()
            for j in range(i, N):
                counter[nums[j]] += 1
                if counter[0] == counter[1]:
                    max_length = max(max_length, j - i + 1)
        
        return max_length
        
# sliding windows - TLE
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        counter = Counter(nums)
        N = len(nums)
        window = N
        while window >= 2:
            for i in range(0, N-window + 1):
                counter = Counter(nums[i:i+window])
                if counter[0] == counter[1]:
                    return window
            
            window -= 1
        return 0