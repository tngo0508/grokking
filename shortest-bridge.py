from collections import deque

def mark_island(row, col, grid, val):
    q = deque([[row, col]])
    while q:
        r, c = q.popleft()
        grid[r][c] = val
        for x, y in [[0, 1], [1,0],[0,-1],[-1,0]]:
            new_row, new_col = r + x, c + y
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                q.append([new_row, new_col])


def bfs(row, col, clone_grid):
    q = deque([[row, col, 0]])
    while q:
        r, c, dist = q.popleft()
        for x, y in [[0, 1], [1,0],[0,-1],[-1,0]]:
            new_row, new_col = r + x, c + y
            if 0 <= new_row < len(clone_grid) and 0 <= new_col < len(clone_grid[0]):
                if clone_grid[new_row][new_col] == 0:
                    q.append([new_row, new_col, dist + 1])
                    clone_grid[new_row][new_col] = dist + 1
                elif clone_grid[new_row][new_col] == '$':
                    return dist

    return float('inf')

    

def shortest_bridge(grid):
    result = float('inf')
    num_rows = len(grid)
    num_cols = len(grid[0])
    for row in range(num_rows):
        stop = False
        for col in range(num_cols):
            if grid[row][col] == 1:
                mark_island(row, col, grid, '#')
                stop = True
                break
        if stop:
            break
    

    for row in range(num_rows):
        stop = False
        for col in range(num_cols):
            if grid[row][col] == 1:
                mark_island(row, col, grid, '$')
                stop = True
                break
        if stop:
            break
    
    print(grid)

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == '#':
                copied_grid = [row[:] for row in grid]
                result = min(result, bfs(row, col, copied_grid))

    
    return result if result != float('inf') else 0


print(shortest_bridge([[0,1,1],[1,0,1],[1,0,1]]))
print(shortest_bridge([[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]))
print(shortest_bridge([[1, 0, 0], [1, 0, 0], [0, 0, 1]]))
print(shortest_bridge([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]))
print(shortest_bridge(
[[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1]]))