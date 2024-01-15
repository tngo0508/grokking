# brute force - TLE
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            return self.longestCommonSubsequence(text2, text1)

        t1 = text1
        t2 = text2
        def dfs(t1_idx, t2_idx):
            if t1_idx == len(text1):
                return 0
            if t2_idx == len(text2):
                return 0

            if t1[t1_idx] == t2[t2_idx]:
                return dfs(t1_idx + 1, t2_idx + 1) + 1
            
            return max(dfs(t1_idx + 1, t2_idx), dfs(t1_idx, t2_idx + 1))

# Memoization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            return self.longestCommonSubsequence(text2, text1)

        t1 = text1
        t2 = text2
        memo = {}
        def dfs(t1_idx, t2_idx):
            if t1_idx == len(text1):
                return 0
            if t2_idx == len(text2):
                return 0

            if (t1_idx, t2_idx) in memo:
                return memo[(t1_idx, t2_idx)]

            if t1[t1_idx] == t2[t2_idx]:
                return dfs(t1_idx + 1, t2_idx + 1) + 1
            
            result = max(dfs(t1_idx + 1, t2_idx), dfs(t1_idx, t2_idx + 1))
            memo[(t1_idx, t2_idx)] = result
            return result

        return dfs(0, 0)