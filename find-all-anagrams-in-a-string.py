class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        counter_p = Counter(p)
        counter = Counter()
        start = end = 0
        for end in range(len(s)):
            counter[s[end]] += 1
            
            while counter[s[end]] > counter_p[s[end]]:
                counter[s[start]] -= 1
                if counter[s[start]] <= 0:
                    del counter[s[start]]
                start += 1
            
            if counter == counter_p:
                res.append(start)
        
        return res
