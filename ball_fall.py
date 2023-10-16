import pprint


def traverse(row, col, grid, n, m, result):
    i = col
    while True:
        if not (0 <= row < n and 0 <= col < m):
            break
        if row == n - 1 and 0 <= col < m:
            if grid[row][col] == -1:
                if col - 1 >= 0:
                    result[i] = col - 1
                else:
                    break
            else:
                if col + 1 < m:
                    result[i] = col + 1
                else:
                    break
            break
        if grid[row][col] == 1:
            if 0 <= row < n and 0 <= col + 1 < m and grid[row][col + 1] == -1:
                break
            col += 1
        elif grid[row][col] == -1:
            if 0 <= row < n and 0 <= col - 1 < m and grid[row][col - 1] == 1:
                break
            col -= 1
        row += 1


def find_exit_column(grid):
    pprint.pprint(grid)
    n = len(grid)
    m = len(grid[0])
    result = [-1] * m
    for col in range(m):
        traverse(0, col, grid, n, m, result)

    return result


print(find_exit_column([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1],
                        [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]))
print(find_exit_column([[1, 1, 1, 1, 1, 1], [-1, -1, -1, -
                                             1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]))
print(find_exit_column([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))


# feedback
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

# solution
def find_exit_column(grid):
    result = [-1]*len(grid[0])

    for col in range(len(grid[0])):
        current_col = col

        for row in range(len(grid)):
            next_col = current_col + grid[row][current_col]

            if next_col < 0 or next_col > len(grid[0])-1 or grid[row][current_col] != grid[row][next_col]:
                break

            if row == len(grid)-1:
                result[col] = next_col
            current_col = next_col
    return result