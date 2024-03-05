# My solution - Two pointers - Accepted
class Solution:
    def minimumLength(self, s: str) -> int:
        N = len(s)
        l, r = 0, N - 1
        length = N
        while l < r and s[l] == s[r]:
            ch = s[l]
            while l <= r and s[l] == ch:
                l += 1
            while r > l and s[r] == ch:
                r -= 1
            
            length = min(length, r - l + 1)
        return length