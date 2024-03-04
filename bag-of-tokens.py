# Brute Force - TLE
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        N = len(tokens)

        def dfs(curr_power, curr_score, tokens_arr):
            # print(tokens_arr)
            if set(tokens_arr) == 1 and '#' in tokens_arr:
                return curr_score

            res = 0
            
            for i in range(N):
                # print(tokens_arr, curr_score)
                if tokens_arr[i] != '#':
                    token = tokens_arr[i]
                    tokens_arr[i] = '#'
                    if curr_power >= token:
                        res = max(res, dfs(curr_power - token, curr_score + 1, tokens_arr), curr_score)
                    if curr_score >= 1:
                        res = max(res, dfs(curr_power + token, curr_score - 1, tokens_arr), curr_score)
                    tokens_arr[i] = token
            return max(res, curr_score)

        return dfs(power, 0, tokens)