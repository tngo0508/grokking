class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            grid[r][c] = '0'
            for row, col in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0 <= row < rows and 0 <= col < cols and grid[row][col] != '0':
                    dfs(row, col)
        
        num_of_islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    num_of_islands += 1
        
        return num_of_islands