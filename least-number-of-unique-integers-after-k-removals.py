# My solution
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        temp = [(v, k) for k, v in counter.items()]
        temp.sort(key=lambda x:x[0])

        for freq, num in temp:
            if k < freq:
                break
            k -= freq
            counter[num] -= freq
        
        count = 0
        for k, v in counter.items():
            if v > 0:
                count += 1

        return count