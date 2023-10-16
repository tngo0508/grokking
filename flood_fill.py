def valid(row, col, grid, origin_val):
    if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
        return False
    
    if grid[row][col] != origin_val or grid[row][col] == '*':
        return False

    return True

def backtrack(grid, sr, sc, origin_val, cells):
    if grid[sr][sc] != origin_val:
        return
    
    cells.append([sr, sc])

    for [x, y] in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        if valid(sr + x, sc + y, grid, origin_val):
            grid[sr][sc] = '*'
            backtrack(grid, sr + x, sc + y, origin_val, cells)
            grid[sr][sc] = origin_val

def flood_fill(grid, sr, sc, target):
    if not grid:
        return []
    num_row = len(grid)
    num_col = len(grid[0])

    if not (0 <= sr < num_row) or not (0 <= sc < num_col):
        return []

    origin_val = grid[sr][sc]
    cells = []
    backtrack(grid, sr, sc, origin_val, cells)
    for row, col in cells:
        grid[row][col] = target
    return grid