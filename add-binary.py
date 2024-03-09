# My solution
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(reversed(a))
        b = list(reversed(b))
        len_a = len(a)
        len_b = len(b)
        i = 0
        res = []
        carry = 0
        while i < max(len_a, len_b):
            val_a = int(a[i]) if i < len_a else 0
            val_b = int(b[i]) if i < len_b else 0
            curr_sum = val_a + val_b + carry
            carry = curr_sum // 2
            res.append(str(curr_sum % 2))
            i += 1
        
        if carry:
            res.append(str(carry))

        return ''.join(reversed(res))


# Approach 1: Bit-by-Bit Computation
class Solution:
    def addBinary(self, a, b) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
                
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')
            
            carry //= 2
        
        if carry == 1:
            answer.append('1')
        answer.reverse()
        
        return ''.join(answer)


# Bit manipulation approach
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]