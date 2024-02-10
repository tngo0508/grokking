# My solution
class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindromic(l, r):
            ans = 0
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    ans += 1
                else:
                    break
                l -= 1
                r += 1
            return ans

        res = 0
        for i, c in enumerate(s):
            odd = is_palindromic(i, i)
            even = is_palindromic(i, i + 1)
            res += odd + even
        return res