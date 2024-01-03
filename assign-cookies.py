# Time Limit Exceeded
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        used = set()
        for greed_factor in sorted(g):
            for i, size in enumerate(sorted(s)):
                if size >= greed_factor and i not in used:
                    result += 1
                    used.add(i)
                    break
        return result