def house_robber(money):
    if len(money) < 2:
        return max(money)
    n = len(money)
    dp = [0] * n
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    
    return max(dp[-2], dp[-1] - money[0])

# solution
def house_robber(money):
    if len(money) == 0 or money is None:
        return 0

    if len(money) == 1:
        return money[0]

    return max(house_robber_helper(money[:-1]), house_robber_helper(money[1:]))


def house_robber_helper(money):
    lookup_array = [0 for x in range(len(money) + 1)]
    lookup_array[0] = 0
    lookup_array[1] = money[0]
    for i in range(2, len(money)+1):
        lookup_array[i] = max(money[i-1]+lookup_array[i-2], lookup_array[i-1])

    return lookup_array[len(money)]