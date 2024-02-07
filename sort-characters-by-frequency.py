# My solution
class Solution:
    def frequencySort(self, s: str) -> str:
        counter_s = Counter(s)
        arr = []
        for c, freq in counter_s.items():
            arr.append([freq, c])

        arr.sort(reverse=True)
        res = []
        for freq, c in arr:
            res.append(c * freq)
        
        return ''.join(res)