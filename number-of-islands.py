class UnionFind:

    # Initializing the parent list and count variable by traversing the grid
    def __init__(self, grid):
        self.parent = []
        self.rank = []
        self.count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent.append(i * n + j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    # Function to find the root parent of a node
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # Function to connect components
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1

    # Function to return the number of conencted components consisting of "1"s
    def get_count(self):
        return self.count

from union_find import UnionFind

def connect(row, col, grid, uf):
    for x, y in [(0, 1),(0, -1),(1, 0),(-1, 0)]:
        r = row + x
        c = col + y
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
            uf.union(row * len(grid[0]) + col, r * len(grid[0]) + c)
            

def num_islands(grid):
    n = len(grid)
    m = len(grid[0])
    uf = UnionFind(grid)
    print(uf.get_count())
    for row in range(n):
        for col in range(m):
            if grid[row][col] == "1":
                grid[row][col] = "0"
                connect(row, col, grid, uf)
    
    print(uf.parent)
    return uf.get_count()

# SOLUTION
from union_find import UnionFind

def num_islands(grid):
    if not grid:
        return 0

    cols = len(grid[0])
    rows = len(grid)
    union_find = UnionFind(grid)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                grid[r][c] = '0'

                if r - 1 >= 0 and grid[r - 1][c] == '1':
                    union_find.union(r * cols + c, (r - 1) * cols + c)
                if r + 1 < rows and grid[r + 1][c] == '1':
                    union_find.union(r * cols + c, (r + 1) * cols + c)
                if c - 1 >= 0 and grid[r][c - 1] == '1':
                    union_find.union(r * cols + c, r * cols + c - 1)
                if c + 1 < cols and grid[r][c + 1] == '1':
                    union_find.union(r * cols + c, r * cols + c + 1)

    count = union_find.get_count()
    return count
