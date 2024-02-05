# my solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = OrderedDict()
        for i, c in enumerate(s):
            if c not in hash_map:
                hash_map[c] = [i, 0]
            hash_map[c][1] += 1

        for i, count in hash_map.values():
            if count == 1:
                return i

        return -1
    
# Editorial Solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map: character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1