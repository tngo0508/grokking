class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hash_map = defaultdict(int)
        for word in words:
            for c in word:
                hash_map[c] += 1

        
        for v in hash_map.values():
            if v % len(words) != 0:
                return False
        
        return True
