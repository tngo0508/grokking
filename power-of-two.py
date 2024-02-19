# Brute force
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            n = n / 2
        return n == 1
    
# No loop/recursion with library
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        return bin(n).count("1") == 1
    
# Approach 1: Bitwise Operators: Get the Rightmost 1-bit
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (-n) == n
    
# Approach 2: Bitwise operators: Turn off the Rightmost 1-bit
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (n - 1) == 0