class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        N = len(nums)

        for i in range(0, N, 3):
            arr = [nums[i]]
            j = i + 1
            while len(arr) < 3 and abs(nums[j] - arr[-1]) <= k:
                arr.append(nums[j])
                j += 1
            
            if len(arr) < 3:
                return []
            
            if abs(arr[0] - arr[-1]) > k:
                return []

            res.append(arr[:])        
        return res

# Editorial Solution
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append([nums[i], nums[i + 1], nums[i + 2]])
        return ans