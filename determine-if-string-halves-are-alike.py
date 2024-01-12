class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        left = right = 0
        while l < r:
            left += s[l] in vowels
            right += s[r] in vowels
            l += 1
            r -= 1
        return left == right