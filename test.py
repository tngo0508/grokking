from typing import List

def traverse(row: int, col: int, grid: List[List[int]], num_rows: int, num_cols: int) -> int:
    while 0 <= row < num_rows and 0 <= col < num_cols:
        if row == num_rows - 1:
            if grid[row][col] == -1:
                return col - 1 if col - 1 >= 0 else -1
            else:
                return col + 1 if col + 1 < num_cols else -1
        if grid[row][col] == 1:
            if 0 <= col + 1 < num_cols and grid[row][col + 1] == -1:
                return -1
            col += 1
        elif grid[row][col] == -1:
            if 0 <= col - 1 < num_cols and grid[row][col - 1] == 1:
                return -1
            col -= 1
        row += 1
    return -1

def find_exit_column(grid: List[List[int]]) -> List[int]:
    num_rows = len(grid)
    num_cols = len(grid[0])
    exit_columns = [traverse(0, col, grid, num_rows, num_cols) for col in range(num_cols)]
    return exit_columns