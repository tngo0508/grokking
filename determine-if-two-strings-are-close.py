class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        w1_set = set(word1)
        w2_set = set(word2)
        if w1_set != w2_set:
            return False

        w1_counter = Counter(word1)
        w2_counter = Counter(word2)

        values1 = w1_counter.values()
        values2 = w2_counter.values()

        return sorted(values1) == sorted(values2)

