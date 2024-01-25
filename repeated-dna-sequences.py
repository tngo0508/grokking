class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        hash_map = defaultdict(int)
        start = 0
        for end in range(len(s)):
            if end - start + 1 >= 10:
                curr_str = s[start:end + 1]
                hash_map[curr_str] += 1
                start += 1

        return [strg for strg, v in hash_map.items() if v > 1]

# Solution
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)     
        seen, output = set(), set()

        # iterate over all sequences of length L
        for start in range(n - L + 1):
            tmp = s[start:start + L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return output