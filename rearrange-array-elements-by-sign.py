# My solution
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = deque()
        negatives = deque()
        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)
        
        if not positives:
            return []

        res = [positives.popleft()]
        while positives and negatives:
            if res[-1] > 0:
                res.append(negatives.popleft())
            else:
                res.append(positives.popleft())
        
        res.extend(positives)
        res.extend(negatives)

        return res
    
# Editorial Solution
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Initializing an answer array of size n
        ans = [0] * n

        # Initializing two pointers to track even and
        # odd indices for positive and negative integers respectively
        pos_index, neg_index = 0, 1

        for i in range(n):
            if nums[i] > 0:
                # Placing the positive integer at the
                # desired index in ans and incrementing pos_index by 2
                ans[pos_index] = nums[i]
                pos_index += 2
            else:
                # Placing the negative integer at the
                # desired index in ans and incrementing neg_index by 2
                ans[neg_index] = nums[i]
                neg_index += 2

        return ans