class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        num_of_elems = rows * cols
        res = []
        row = col = 0
        while row < rows and col < cols:
            # top left -> top right
            for c in range(col, cols - col):
                res.append(matrix[row][c])
            
            if len(res) == num_of_elems:
                break

            # top right -> bottom right
            for r in range(row + 1, rows - row -1):
                res.append(matrix[r][cols - col - 1])


            # bottom right -> bottom left
            for c in range(cols - col - 1, col - 1, -1):
                res.append(matrix[rows - row - 1][c])

            if len(res) == num_of_elems:
                break

            # bottom left -> top left
            for r in range(rows - row - 2, row, -1):
                res.append(matrix[r][col])

            row += 1
            col += 1
        return res