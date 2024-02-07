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
    
# Editorial solution - bucket sort
def frequencySort(self, s: str) -> str:
    if not s: return s

    # Determine the frequency of each character.
    counts = collections.Counter(s)
    max_freq = max(counts.values())

    # Bucket sort the characters by frequency.
    buckets = [[] for _ in range(max_freq + 1)]
    for c, i in counts.items():
        buckets[i].append(c)

    # Build up the string.
    string_builder = []
    for i in range(len(buckets) - 1, 0, -1):
        for c in buckets[i]:
            string_builder.append(c * i)

    return "".join(string_builder)