# Brute Force - BFS - Memory Limit Exceeded
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        res = float('inf')
        N = len(matrix)
        queue = deque()
        for col, x in enumerate(matrix[0]):
            queue.append([0, col, x])
        
        while queue:
            row, col, curr_sum = queue.popleft()
            if row == N - 1:
                res = min(res, curr_sum)
            for col in [col - 1, col, col + 1]:
                if 0 <= col < N and 0 <= row + 1 < N:
                    queue.append([row + 1, col, curr_sum + matrix[row + 1][col]])
        
        return res
    
    
# DP
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)

        for row in range(1, N):
            for col in range(N):
                temp = matrix[row][col]
                val = float('inf') 
                for c in [col - 1, col, col + 1]:
                    if 0 <= c < N:
                        val = min(val, temp + matrix[row - 1][c])
                matrix[row][col] = val

        
        return min(matrix[-1])
