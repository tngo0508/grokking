# Brute Force
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(curr_str):
            if len(curr_str) >= len(s):
                if curr_str == s:
                    return True
                return False
            
            res = False
            for word in wordDict:
                if dfs(curr_str + word):
                    res = True
                    break
            
            return res

        return dfs("")
    
# Dynamic programming
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True # empty string -> True
        start = 0

        for i in range(1, N + 1):
            j = i - 1
            while j >= 0:
                curr = s[j:i]
                if curr in wordDict and dp[i - len(curr)]:
                    dp[i] = True
                    break
                j -= 1

        return dp[-1]
