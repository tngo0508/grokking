# My solution
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        curr_max = 0
        for num in nums:
            freq[num] += 1
            curr_max = max(freq[num], curr_max)

        
        res = 0
        for value in freq.values():
            if value == curr_max:
                res += value
        return res