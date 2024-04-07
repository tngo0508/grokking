# My solution - memoization
class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        memo = defaultdict()
        def dfs(index, balance):
            if index == N:
                return balance == 0

            if balance < 0:
                return False

            if (index, balance) in memo:
                return memo[(index, balance)]

            res = False
            if s[index] == '(':
                res = dfs(index + 1, balance + 1)
            elif s[index] == ')':
                res = dfs(index + 1, balance - 1)
            else:
                res = dfs(index + 1, balance) or dfs(index + 1, balance + 1) or dfs(index + 1, balance - 1)
            
            memo[(index, balance)] = res
            return res

        return dfs(0, 0)