class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for row in range(n):
            for col in range(n):
                if isConnected[row][col] == 1:
                    uf.union(row, col)
        
        for i in range(n):
            uf.find(i)
        
        return len(set(uf.root))
        
        
        
# LEETCODE SOLUTION
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        num_of_provinces = n
        for row in range(n):
            for col in range(row + 1, n):
                if isConnected[row][col] == 1 and uf.find(row) != uf.find(col):
                    num_of_provinces -= 1
                    uf.union(row, col)
        
        return num_of_provinces
        
        
        
        