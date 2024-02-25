# UnionFind - TLE
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0] * n

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
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def gcd(a, b): # Euclidean Algorithm 
            while b:
                a, b = b, a % b
            return a

        edges = []
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                if gcd(nums[i], nums[j]) > 1:
                    edges.append([i, j])

        uf = UnionFind(N)
        for x, y in edges:
            uf.union(x, y)
        
        for i in range(N):
            uf.find(i)

        
        return len(set(uf.root)) == 1