# BRUTE FORCE - TIME LIMIT EXCEEDED
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)
        memo = defaultdict()
        
        def dfs(i, open_count, close_count):
            if close_count > open_count:
                return

            if i == N:
                return

            if s[i] == '(':
                open_count += 1
            else:
                close_count += 1
            
            if open_count == close_count:
                dfs.result = max(dfs.result, open_count * 2) 
            dfs(i + 1, open_count, close_count)
        
        dfs.result = 0
        for i in range(N):
            if s[i] == '(':
                dfs(i, 0, 0)
        return dfs.result

# Editorial solution - stack
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with a sentinel value
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if not stack:
                        stack.append(i)
                    else:
                        max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)

        return max_len
    
# Editorial solution - Dynamic programming
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Get the length of the input string
        n = len(s)
        
        # Initialize an array to store the length of valid parentheses substrings ending at each position
        dp = [0] * n
        
        # Variable to keep track of the maximum valid length
        max_len = 0

        # Iterate through the input string starting from the second character
        for i in range(1, n):
            # Check if the current character is ')'
            if s[i] == ')':
                # Case 1: If the previous character is '(', update dp[i] based on the length of the valid substring ending at i-2 (if i >= 2)
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                # Case 2: If the previous character is ')' and there is a valid substring ending at i-1, consider its length as well
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
                
                # Update max_len with the current maximum length
                max_len = max(max_len, dp[i])

        # Return the final result, which is the maximum valid length
        return max_len

