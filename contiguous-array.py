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

# Solution
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        sum_index_map = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in sum_index_map:
                max_length = max(max_length, i - sum_index_map[count])
            else:
                sum_index_map[count] = i

        return max_length
    
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen_at = {0: -1}
        max_len = count = 0

        for i, n in enumerate(nums):
            count += (1 if n else -1)
            if count in seen_at:
                max_len = max(max_len, i - seen_at[count])
            else:
                seen_at[count] = i
        return max_len