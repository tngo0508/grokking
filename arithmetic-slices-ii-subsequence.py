# BRUTE FORCE - TIME LIMIT EXCEEDED
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        def dfs(index, nums, curr):
            if index == N:
                if len(curr) < 3:
                    return

                # check difference
                diff = curr[1] - curr[0]
                for i in range(2, len(curr)):
                    if curr[i] - curr[i - 1] != diff:
                        return
                dfs.result += 1
                return

            
            dfs(index + 1, nums, curr) # skip
            dfs(index + 1, nums, curr + [nums[index]]) # take

        dfs.result = 0
        dfs(0, nums, [])
        return dfs.result
    
