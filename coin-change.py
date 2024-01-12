# Brute Force
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        result = float('inf')

        def dfs(idx, amount, curr):
            nonlocal result
            if amount < 0:
                return
            if amount == 0:
                result = min(result, len(curr))
                return

            for i in range(idx, N):
                dfs(i, amount - coins[i], curr + [coins[i]])

        dfs(0, amount, [])
        return result if result != float('inf') else -1
    
# Brute force - different implementation
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)

        def dfs(idx, curr_amount):
            if curr_amount == 0:
                return 0

            if curr_amount < 0:
                return float('inf')

            num_of_coins = []
            for i in range(idx, N):
                num_of_coins.append(dfs(i, curr_amount - coins[i]) + 1)
            
            return min(num_of_coins)


        result = dfs(0, amount)
        return result if result != float('inf') else -1
    
# Memoization Approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        memo = defaultdict()
        def dfs(idx, curr_amount):
            if curr_amount == 0:
                return 0

            if curr_amount < 0:
                return float('inf')
            
            if (idx, curr_amount) in memo:
                return memo[(idx, curr_amount)]

            num_of_coins = []
            for i in range(idx, N):
                num_of_coins.append(dfs(i, curr_amount - coins[i]) + 1)

            memo[(idx, curr_amount)] = min(num_of_coins)
            
            return memo[(idx, curr_amount)]


        result = dfs(0, amount)
        return result if result != float('inf') else -1
    
# Cleaner Memoization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict()
        def dfs(curr_amount):
            if curr_amount == 0:
                return 0

            if curr_amount < 0:
                return float('inf')
            
            if curr_amount in memo:
                return memo[curr_amount]

            num_of_coins = []
            for coin in coins:
                num_of_coins.append(dfs(curr_amount - coin) + 1)

            memo[curr_amount] = min(num_of_coins)
            
            return memo[curr_amount]


        result = dfs(amount)
        return result if result != float('inf') else -1