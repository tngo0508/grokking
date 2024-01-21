class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        start = 0
        res = float('-inf')
        hash_map = defaultdict(int)
        for i, c in enumerate(s):
            if c not in hash_map:
                hash_map[c] = i
            else:
                res = max(res, i - hash_map[c] - 1)

        return res if res != float('-inf') else -1