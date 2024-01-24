class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        def swap_horizontal():
            for row in range(N):
                l, r = 0, N - 1
                while l < r:
                    matrix[row][l], matrix[row][r] = matrix[row][r], matrix[row][l]
                    l += 1
                    r -= 1

        def swap_diagonal():
            swap_diagonal_helper(row=True)
            swap_diagonal_helper(row=False)

        def helper(row, col):
            temp = []
            while row < N and col < N:
                temp.append([row, col])
                row += 1
                col += 1
                
            l, r = 0, len(temp) - 1
            while l < r:
                l_row, l_col = temp[l]
                r_row, r_col = temp[r]
                matrix[l_row][l_col], matrix[r_row][r_col] = matrix[r_row][r_col], matrix[l_row][l_col]
                l += 1
                r -= 1

        def swap_diagonal_helper(row=True):
            if row:
                for col in range(N):
                    helper(0, col)
            else:
                for row in range(1, N):
                    helper(row, 0)

        swap_horizontal()
        swap_diagonal()

        return matrix
