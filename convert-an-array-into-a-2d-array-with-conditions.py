from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        result = []
        N = len(nums)
        n = 0
        while n < N:
            curr = []
            for k, v in counter.items():
                if v > 0:
                    curr.append(k)
                    counter[k] -= 1
            result.append(curr[:])
            n += len(curr)
        return result    