class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = [0] * 26
        for c in magazine:
            i = ord(c) - ord('a')
            letters[i] += 1
        
        for c in ransomNote:
            i = ord(c) - ord('a')
            letters[i] -= 1
            if letters[i] < 0:
                return False
        
        return True