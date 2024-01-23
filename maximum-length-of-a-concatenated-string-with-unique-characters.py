class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        def isValid(curr):
            curr_str = ''.join(curr)
            return len(curr_str) == len(set(curr_str))

        def dfs(idx, curr):
            if not isValid(curr):
                return 0

            if idx == N:
                return len(''.join(curr))
            
            return max(dfs(idx + 1, curr + [arr[idx]]), dfs(idx + 1, curr))

        return dfs(0, [])