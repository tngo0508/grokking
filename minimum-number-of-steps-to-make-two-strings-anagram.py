class Solution:
    def minSteps(self, s: str, t: str) -> int:
        num_of_chars = ord('z') - ord('a')
        chars = [0] * (num_of_chars + 1)
        for c in s:
            i = ord(c) - ord('a')
            chars[i] += 1

        for c in t:
            i = ord(c) - ord('a')
            chars[i] -= 1
        
        result = 0
        for freq in chars:
            if freq >= 1:
                result += freq
        return result
