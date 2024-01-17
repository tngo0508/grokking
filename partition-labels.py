class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        N = len(s)
        res = []
        hash_map = OrderedDict()
        for i, c in enumerate(s):
            hash_map[c] = i

        start = end = 0
        for c, idx in hash_map.items():
            left_set = set(s[:idx])
            right_set = set(s[idx:])
            end = idx
            partition = True
            for ch in left_set:
                if ch != c and ch in right_set:
                    partition = False
                    break
            
            if partition:
                res.append(end - start + 1)
                start = end + 1
        return res