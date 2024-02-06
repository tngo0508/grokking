# My solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for s in strs:
            hash_map[tuple(sorted(s))].append(s)
        
        return hash_map.values()