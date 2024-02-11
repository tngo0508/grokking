# My solution
class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        dp = [1] * N
        for i in range(N):
            l = i - 1 if i > 0 else i
            r = i + 1 if i + 1 < N else i
            if ratings[i] > ratings[l]:
                dp[i] = max(dp[i], dp[l] + 1)
            if ratings[i] > ratings[r]:
                dp[i] = max(dp[i], dp[r] + 1)
        
        for i in reversed(range(N)):
            l = i - 1 if i > 0 else i
            r = i + 1 if i + 1 < N else i
            if ratings[i] > ratings[l]:
                dp[i] = max(dp[i], dp[l] + 1)
            if ratings[i] > ratings[r]:
                dp[i] = max(dp[i], dp[r] + 1)
        return sum(dp)