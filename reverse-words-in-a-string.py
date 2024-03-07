# My solution
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        N = len(s)
        curr = []
        for i in reversed(range(N)):
            if not s[i].isalnum() and curr:
                res.append(''.join(curr[::-1]))
                curr = []
            
            if s[i].isalnum():
                curr.append(s[i])
        
        if curr:
            res.append(''.join(curr[::-1]))
        return ' '.join(res)
    
