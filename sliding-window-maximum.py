# Brute force - TLE
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        res = []
        for end in range(len(nums)):
            if end - start + 1 == k:
                res.append(max(nums[start:end+1]))
                start += 1
        return res
    
# Monotonic Decreasing Queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        
        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            res.append(nums[dq[0]])
        
        return res