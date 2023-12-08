class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      matrix = [[1 for _ in range(m)] for _ in range(n)]
      for row in range(1, n):
        for col in range(1, m):
          matrix[row][col] = matrix[row - 1][col] + matrix[row][col - 1]
      
      return matrix[-1][-1]
            