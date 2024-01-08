class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            prev = result[-1]
            curr = prev[:]
            curr.append(1)
            for j in range(1, len(prev)):
                curr[j] = prev[j - 1] + prev[j]
            result.append(curr[:])
        
        return result