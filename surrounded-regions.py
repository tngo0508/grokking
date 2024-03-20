# My solution
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        not_flipped_cells = deque()
        for r in range(ROWS):
            if board[r][0] == "O":
                not_flipped_cells.append([r, 0])
            if board[r][COLS - 1] == "O":
                not_flipped_cells.append([r, COLS - 1])
        
        for c in range(COLS):
            if board[0][c] == "O":
                not_flipped_cells.append([0, c])
            if board[ROWS - 1][c] == "O":
                not_flipped_cells.append([ROWS-1, c])
        
        while not_flipped_cells:
            row, col = not_flipped_cells.popleft()
            if board[row][col] in ("X", "2"):
                continue
            board[row][col] = "2"
            for x, y in ([0,1],[1,0],[0,-1],[-1,0]):
                r, c = row + x, col + y
                if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == "O":
                    not_flipped_cells.append([r,c])

        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "2":
                    board[r][c] = "O"