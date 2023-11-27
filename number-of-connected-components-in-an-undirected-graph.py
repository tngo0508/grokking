class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = self.root[root_y]
            elif self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = self.root[root_x]
            else:
                self.root[root_y] = self.root[root_x]
                self.rank[root_x] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        
        for i in range(n):
            uf.find(i)

        return len(set(uf.root))
    

# leetcode solution
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.components = 0

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return 0

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = self.root[root_y]
            elif self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = self.root[root_x]
            else:
                self.root[root_y] = self.root[root_x]
                self.rank[root_x] += 1
            
            return 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        num_of_components = n
        for a, b in edges:
            num_of_components -= (uf.union(a, b))

        return num_of_components
    

