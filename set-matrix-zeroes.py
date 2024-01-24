class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        queue = deque()
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    queue.append([row, col])
        
        while queue:
            row, col = queue.popleft()
            for c in range(cols):
                matrix[row][c] = 0
            for r in range(rows):
                matrix[r][col] = 0
        
        return matrix