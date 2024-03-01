class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counter = Counter(s)
        if counter['1'] > 0:
            N = len(s)
            res = ['0'] * N
            res[-1] = '1'
            counter['1'] -= 1
            i = 0
            while counter['1'] > 0:
                res[i] = '1'
                counter['1'] -= 1
                i += 1
            return ''.join(res)
        return s