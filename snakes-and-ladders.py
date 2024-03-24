# My solution
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        def num_to_cell():
            hash_map = defaultdict()
            left_to_right = True
            number = 1
            for i in range(N - 1, -1, -1):
                if left_to_right:
                    for j in range(N):
                        hash_map[number] = (i, j)
                        number += 1
                else:
                    for j in range(N - 1, -1, -1):
                        hash_map[number] = (i, j)
                        number += 1
                left_to_right = not left_to_right
            return hash_map
        
        num_to_cell_map = num_to_cell()
        queue = deque()
        queue.append([1, 0])
        visited = set()
        while queue:
            curr, moves = queue.popleft()
            
            for next_num in range(curr + 1, min(curr + 6, N * N) + 1):
                r, c = num_to_cell_map[next_num]

                next_node = board[r][c] if board[r][c] != -1 else next_num

                if next_node == N * N:
                    return moves + 1

                if next_node not in visited:
                    visited.add(next_node)
                    queue.append([next_node, moves + 1])
        return -1


# Solution
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r,c]
        
        q = deque()
        q.append([1,0])  # [squares,moves]
        visit = set()
        while q:
            squares,moves = q.popleft()
            for i in range(1,7):
                nextSquare = squares + i
                r,c = intToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == length*length:
                    return moves + 1
                if nextSquare not in visit:
                    q.append([nextSquare,moves+1])
                    visit.add(nextSquare)
        return -1

# Editorial Solution
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n**2 + 1)
        label = 1
        columns = list(range(0, n))
        for row in range(n - 1, -1, -1):
            for column in columns:
                cells[label] = (row, column)
                label += 1
            columns.reverse()
        dist = [-1] * (n * n + 1)
        q = deque([1])
        dist[1] = 0
        while q:
            curr = q.popleft()
            for next in range(curr + 1, min(curr + 6, n**2) + 1):
                row, column = cells[next]
                destination = (board[row][column] if board[row][column] != -1
                               else next)
                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    q.append(destination)
        return dist[n * n]