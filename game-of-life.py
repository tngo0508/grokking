# My solution
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = deque()
        hash_set = set()
        ROWS = len(board)
        COLS = len(board[0])
        clone = [[board[r][c] for c in range(COLS)] for r in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                total = 0
                for x, y in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                    row = r + x
                    col = c + y
                    if 0 <= row < ROWS and 0 <= col < COLS:
                        total += board[row][col]
                
                if total == 3:
                    clone[r][c] = 1
                elif total < 2 or total > 3:
                    clone[r][c] = 0
        
        
        for r in range(ROWS):
            for c in range(COLS):
                board[r][c] = clone[r][c]

        