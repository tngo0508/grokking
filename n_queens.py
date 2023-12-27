# time limit exceeded
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check_row(c, cols):
            return c not in cols
        
        def check_col(r, rows):
            return r not in rows
        
        def check_diagonal(r, c, diagonal, rev_diagonal):
            return (c - r) not in diagonal and (c + r) not in rev_diagonal 

        def is_valid(r, c, diagonal, rev_diagonal, cols, rows):
            return check_row(c, cols) and check_col(r, rows) and check_diagonal(r, c, diagonal, rev_diagonal)

        def backtrack(n, n_queens, board, result, diagonal, rev_diagonal, cols, rows):
            if n_queens == 0:
                candidate = ["".join(x) for x in board]
                if candidate not in result:
                    result.append(["".join(x) for x in board])
                return

            for i in range(n):
                for j in range(n):
                    if is_valid(i, j, diagonal, rev_diagonal, cols, rows):
                        board[i][j] = 'Q'
                        diagonal.append(j-i)
                        rev_diagonal.append(i+j)
                        rows.append(i)
                        cols.append(j)

                        backtrack(n, n_queens - 1, board, result, diagonal, rev_diagonal, cols, rows)

                        diagonal.pop()
                        rev_diagonal.pop()
                        rows.pop()
                        cols.pop()
                        board[i][j] = '.'

        
        board = [['.'] * n for _ in range(n)]
        result = []
        backtrack(n, n, board, result, [], [], [], [])
        return result