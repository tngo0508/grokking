class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = []
        rows = len(board)
        cols = len(board[0])

        def backtrack(index, board, r, c, word):
            if index == len(word):
                return True
            temp = board[r][c]
            board[r][c] = '*'
            for x, y in [(1,0),(0,1),(-1,0),(0,-1)]:
                row, col = r - x, c - y
                if 0 <= row < rows and 0 <= col < cols and board[row][col] == word[index]:
                    if backtrack(index + 1, board, row, col, word):
                        return True

            board[r][c] = temp
            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if backtrack(1, board, row, col, word):
                        return True
        
        return False