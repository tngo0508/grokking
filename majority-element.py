# solution - hash map
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_map = defaultdict(int)
        result = [0, nums[0]]
        for num in nums:
            hash_map[num] += 1
            if result[0] < hash_map[num]:
                result = [hash_map[num], num]
        
        return result[1]
    

# optimized solution O(1) space
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate