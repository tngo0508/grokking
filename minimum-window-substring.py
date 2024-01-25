class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = float('inf')
        res = ""
        t_counter = Counter(t)
        t_set = set(t)
        counter = Counter()
        letter_set = set()
        start = 0
        for end, c in enumerate(s):
            counter[c] += 1
            if c in t_set:
                letter_set.add(c)
            if letter_set == t_set:
                for c in t_counter:
                    if counter[c] < t_counter[c]:
                        break
                else:
                    while start <= end and letter_set == t_set:
                        if length >= end - start + 1:
                            length = end - start + 1
                            res = s[start:end + 1]

                        counter[s[start]] -= 1
                        if counter[s[start]] == 0:
                            del counter[s[start]]
                        
                        if counter[s[start]] < t_counter[s[start]]:
                            if s[start] in letter_set:
                                letter_set.remove(s[start])
                        
                        start += 1

        return res

        
