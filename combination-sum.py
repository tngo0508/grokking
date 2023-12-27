class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index, cands, result, curr, target):
            if sum(curr) == target:
                result.append(curr)
                return
            
            if index >= len(cands) or sum(curr) > target:
                return

            for i in range(index, len(cands)):
                backtrack(i, cands, result, curr + [cands[i]], target)


        candidates = list(set(candidates))
        result = []
        backtrack(0, candidates, result, [], target)
        return result