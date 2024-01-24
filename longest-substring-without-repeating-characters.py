class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        longest = 0
        for end, c in enumerate(s):
            while c in seen and start <= end:
                seen.remove(s[start])
                start += 1
            seen.add(c)
            longest = max(longest, end - start + 1)
        return longest

        