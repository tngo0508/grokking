class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindromeLength(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        result = ""
        curr_length = 0
        for i in range(len(s)):
            t1 = getPalindromeLength(i, i)
            t2 = getPalindromeLength(i, i + 1)
            t1 = t2 if len(t2) > len(t1) else t1
            if len(t1) > curr_length:
                result = t1
                curr_length = len(t1)
        
        return result