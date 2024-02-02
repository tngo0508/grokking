# My BFS approach
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        queue = deque()
        for i in range(1, 10):
            queue.append(i)
        
        res = []
        while queue:
            num = queue.popleft()
            if num > high:
                break
            if num >= low:
                res.append(num)
            if (num % 10) + 1 <= 9:
                next_num = (num * 10) + ((num % 10) + 1)
                queue.append(next_num)
            
        return res

# Editorial solution - sliding window
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        n = 10
        nums = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(n - length):
                num = int(sample[start: start + length])
                if num >= low and num <= high:
                    nums.append(num)
        
        return nums