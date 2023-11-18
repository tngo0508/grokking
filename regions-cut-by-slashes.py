class UnionFind:
    # Constructor
    def __init__(self, n):
        self.parent = [0] * n
        self.rank = [1] * n
        for i in range(n):
            self.parent[i] = i
        
    # Function to find which subset a particular element belongs to.
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    # Function to join two subsets into a single subset.
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
                self.rank[p1] = self.rank[p1] + self.rank[p2]
            else:
                self.parent[p1] = p2
                self.rank[p2] = self.rank[p2] + self.rank[p1]

# SOLUTION
from union_find import UnionFind

def regions_by_slashes(grid):
    N = len(grid)
    find_union = UnionFind(4 * N * N)

    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            root = 4 * (r * N + c)

            if val in '/ ': 
                find_union.union(root + 0, root + 1)
                find_union.union(root + 2, root + 3)

            if val in '\ ':
                find_union.union(root + 0, root + 2)
                find_union.union(root + 1, root + 3)

            if r+1 < N:
                find_union.union(root + 3, (root + 4 * N) + 0)

            if r-1 >= 0:
                find_union.union(root + 0, (root - 4 * N) + 3)
            
            if c+1 < N:
                find_union.union(root + 2, (root + 4) + 1)

            if c-1 >= 0:
                find_union.union(root + 1, (root - 4) + 2)

    return sum(find_union.find(x) == x for x in range(4 * N * N))

# driver code
def main():
    inputs = [["/\\", "\\/"], [" /", "  "], [" /", "/ "],
              [" /\\", "\\/ ", ' \\ '], [' \\/', " /\\", "\\/ "]]
    for i in range(len(inputs)):
        print(i + 1, '.\tInput list of strings: ', inputs[i], sep="")
        print('\tOutput: ', regions_by_slashes(inputs[i]))
        print('-' * 100)


if __name__ == "__main__":
    main()

# LEETCODE SOLUTION
class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def regionsBySlashes(self, grid):
        N = len(grid)
        dsu = DSU(4 * N * N)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r*N + c)
                if val in '/ ':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if val in '\ ':
                    dsu.union(root + 0, root + 2)
                    dsu.union(root + 1, root + 3)

                # north/south
                if r+1 < N: dsu.union(root + 3, (root+4*N) + 0)
                if r-1 >= 0: dsu.union(root + 0, (root-4*N) + 3)
                # east/west
                if c+1 < N: dsu.union(root + 2, (root+4) + 1)
                if c-1 >= 0: dsu.union(root + 1, (root-4) + 2)

        return sum(dsu.find(x) == x for x in range(4*N*N))