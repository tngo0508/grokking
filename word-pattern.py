# Brute force
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split()
        unique_words = []
        for word in ss:
            if word not in unique_words:
                unique_words.append(word)

        prev = ''
        hash_map = defaultdict()
        for c in pattern:
            if prev != c:
                prev = c
                if unique_words and c not in hash_map:
                    hash_map[c] = unique_words[0]
                    unique_words = unique_words[1:]

        res = []
        for c in pattern:
            if c not in hash_map:
                return False
            res.append(hash_map[c])
        
        return res == ss

        