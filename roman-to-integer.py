# my solution
class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {
            'I': 1,  'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        res = 0
        N = len(s)
        for i in range(N - 1):
            if hash_map[s[i]] >= hash_map[s[i + 1]]:
                res += hash_map[s[i]]
            else:
                res -= hash_map[s[i]]
        res += hash_map[s[-1]]
        return res