class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result += n & 1
            n = n >> 1
        return result

# solution
# for any number n, doing a bit-wise AND of nnn and n−1n - 1n−1 flips the least-significant 1-bit in n to 0. 
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n > 0:
            result += 1
            n = n & (n - 1)
        return result