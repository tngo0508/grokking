# Brute force - slicing TLE
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(w1, w2):
            # Base case: If w1 is empty, return the length of w2
            if not w1:
                # If w1 is empty, inserting each character of w2 is required
                return len(w2)
            
            # Base case: If w2 is empty, return the length of w1
            if not w2:
                # If w2 is empty, deleting each character from w1 is required
                return len(w1)
            
            # If the current characters of w1 and w2 are the same,
            # move to the next characters without any additional cost
            if w1[0] == w2[0]:
                return dfs(w1[1:], w2[1:])

            # Three possible operations: Insert, Delete, Replace
            # Insert: Move to the next character in w2
            insert = dfs(w1, w2[1:])
            # Delete: Move to the next character in w1
            delete = dfs(w1[1:], w2)
            # Replace: Move to the next characters in both w1 and w2
            replace = dfs(w1[1:], w2[1:])

            # Minimum of the three operations plus 1 (cost of the current operation)
            return min(insert, delete, replace) + 1

        # Start the recursion from the beginning of both words
        return dfs(word1, word2)

# Brute force - use indices TLE
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(i, j):
            # Base case: If w1 is empty, return the length of w2
            if i == len(word1):
                # If w1 is empty, inserting each character of w2 is required
                return len(word2) - j
            
            # Base case: If w2 is empty, return the length of w1
            if j == len(word2):
                # If w2 is empty, deleting each character from w1 is required
                return len(word1) - i
            
            # If the current characters of w1 and w2 are the same,
            # move to the next characters without any additional cost
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            # Three possible operations: Insert, Delete, Replace
            # Insert: Move to the next character in w2
            insert = dfs(i, j + 1)
            # Delete: Move to the next character in w1
            delete = dfs(i + 1, j)
            # Replace: Move to the next characters in both w1 and w2
            replace = dfs(i + 1, j + 1)

            # Minimum of the three operations plus 1 (cost of the current operation)
            return min(insert, delete, replace) + 1

        # Start the recursion from the beginning of both words
        return dfs(0, 0)

# Memoization
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = defaultdict()
        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            insert = dfs(i, j + 1)
            delete = dfs(i + 1, j)
            replace = dfs(i + 1, j + 1)

            result = min(insert, delete, replace) + 1
            memo[(i, j)] = result
            return result

        return dfs(0, 0)
    
# Dynamic programming
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Create a 2D DP table with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize the DP table for base cases
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Fill the DP table using bottom-up dynamic programming
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the current characters match, no additional cost
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Three possible operations: Insert, Delete, Replace
                    # Choose the minimum cost among the three operations
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        # The bottom-right cell of the DP table contains the minimum edit distance
        return dp[m][n]
