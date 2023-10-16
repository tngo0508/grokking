def valid(row: int, col: int, state: List[List[int]], n: int) -> bool:
    not_valid_cell = set()
    for r, c in state:
        for i in range(n):
            not_valid_cell.add((r, i))
            not_valid_cell.add((i, c))
        for i in range(1, n):
            not_valid_cell.add((r + i, c + i))
            not_valid_cell.add((r - i, c - i))
            not_valid_cell.add((r - i, c + i))
            not_valid_cell.add((r + i, c - i))

    return (row, col) not in not_valid_cell


def backtrack(n: int, row: int, state: List[List[int]]) -> int:
    if row > n:
        return 0
    if n == len(state):
        return 1

    count = 0
    for col in range(n):
        if valid(row, col, state, n):
            state.append([row, col])
            count += backtrack(n, row + 1, state)
            state.pop()

    return count


def solve_n_queens(n: int) -> int:
    return backtrack(n, 0, [])