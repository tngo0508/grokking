class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        def find_length(l, r):
            while l >= 0 and r < N and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        result = ""
        max_length = 0
        for i in range(N):
            even = find_length(i, i + 1)
            odd = find_length(i, i)
            length = max(even, odd)
            if max_length < length:
                max_length = length
                half_way = length // 2
                if length % 2 == 0: # even
                    result = s[i - half_way + 1:i + half_way + 1]
                else: # odd
                    result = s[i - half_way:i + half_way + 1]
        
        return result