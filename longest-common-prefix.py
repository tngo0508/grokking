class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        min_length, min_str = min(map(lambda s: (len(s), s), strs))
        while i < min_length:
            c = min_str[i]
            for s in strs:
                if s[i] != c:
                    return min_str[:i]
            
            i += 1
        
        return min_str[:i]