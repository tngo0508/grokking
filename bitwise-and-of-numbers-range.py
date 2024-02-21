# Brute force - TLE
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left
        while left < right:
            left += 1
            res &= left
            if res == 0:
                return 0
        return res
    

# Approach 1: Bit Shift
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0   
        # find the common 1-bits
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift
    
# Approach 2: Brian Kernighan's Algorithm
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            # turn off rightmost 1-bit
            n = n & (n - 1)
        return m & n