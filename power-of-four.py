# Brute force - accepted
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num = 1
        while num <= n:
            if num == n:
                return True
            num = num << 2
        return num == n