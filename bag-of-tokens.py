# Brute Force - TLE
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        N = len(tokens)

        def dfs(curr_power, curr_score, tokens_arr):
            tokens_arr = list(tokens_arr)
            if set(tokens_arr) == 1 and '#' in tokens_arr:
                return curr_score

            res = 0
            
            for i in range(N):
                if tokens_arr[i] != '#':
                    token = tokens_arr[i]
                    tokens_arr[i] = '#'
                    if curr_power >= token:
                        res = max(res, dfs(curr_power - token, curr_score + 1, tuple(tokens_arr)))
                    if curr_score >= 1:
                        res = max(res, dfs(curr_power + token, curr_score - 1, tuple(tokens_arr)))
                    tokens_arr[i] = token
            return max(res, curr_score)

        return dfs(power, 0, tuple(tokens))
    
# Memoization - TLE
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        N = len(tokens)

        def dfs(curr_power, curr_score, tokens_arr):
            if (curr_power, curr_score, tokens_arr) in memo:
                return memo[(curr_power, curr_score, tokens_arr)]

            tokens_arr = list(tokens_arr)
            if set(tokens_arr) == 1 and '#' in tokens_arr:
                return curr_score

            res = 0
            
            for i in range(N):
                if tokens_arr[i] != '#':
                    token = tokens_arr[i]
                    tokens_arr[i] = '#'
                    if curr_power >= token:
                        res = max(res, dfs(curr_power - token, curr_score + 1, tuple(tokens_arr)))
                    if curr_score >= 1:
                        res = max(res, dfs(curr_power + token, curr_score - 1, tuple(tokens_arr)))
                    tokens_arr[i] = token
            
            memo[(curr_power, curr_score, tuple(tokens_arr))] = max(res, curr_score)
            return max(res, curr_score)

        memo = defaultdict(tuple)
        return dfs(power, 0, tuple(tokens))