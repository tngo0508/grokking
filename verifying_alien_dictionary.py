class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = defaultdict()
        for i, c in enumerate(order):
            order_dict[c] = i
        
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if order_dict[c1] > order_dict[c2]:
                        return False
                    else:
                        break
            else:
                if len(w2) < len(w1):
                    return False
                        
        return True
    
# leetcode solution
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):

            for j in range(len(words[i])):
                # If we do not find a mismatch letter between words[i] and words[i + 1],
                # we need to examine the case when words are like ("apple", "app").
                if j >= len(words[i + 1]): return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]: return False
                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    break

        return True