def helper(coins, total, memo):
    if total < 0:
        return -1
    if total == 0:
        return 0
    if total in memo:
        return memo[total]
    
    result = float('inf')
    for coin in coins:
        temp = helper(coins, total - coin, memo)
        if temp >= 0 and temp < result:
            result = temp + 1

    memo[total] = result if result != float('inf') else -1
    return memo[total]

def coin_change(coins, total):
    return helper(coins, total, {})