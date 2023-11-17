class UnionFind:

    # Constructor
    def __init__(self, n):
        self.parent = []
        for i in range(n + 1):
            self.parent.append(i)
        self.rank = [1] * (n + 1)

    # Function to find which subset a particular element belongs to
    def find_parent(self, v):
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find_parent(self.parent[v])
        return self.parent[v]
   
    # Function to join two subsets into a single subset
    def union(self, v1, v2):
        root1 = self.find_parent(v1)
        root2 = self.find_parent(v2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = self.parent[root2]
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = self.parent[root1]
            else:
                self.parent[root2] = self.parent[root1]
                self.rank[root1] += 1
            return False
        return True


def redundant_connection(edges):
    uf = UnionFind(len(edges))
    for x, y in edges:
        if uf.union(x, y):
            return [x, y]
    return edges[-1]

# SOLUTION
class UnionFind:

    def __init__(self, n):
        self.parent = []
        self.rank = rank = [1] * (n + 1)
        for i in range(n + 1):
            self.parent.append(i)

    def find_parent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    def union(self, v1, v2):
        p1, p2 = self.find_parent(v1), self.find_parent(v2)
        if p1 == p2:
            return False
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] = self.rank[p1] + self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] = self.rank[p2] + self.rank[p1]
        
        return True

from union_find import UnionFind

def redundant_connection(edges):
	
	graph = UnionFind(len(edges))
	
	for v1, v2 in edges:
		if not graph.union(v1, v2):
			return [v1, v2]

def main():
	edges = [
		[[1, 2], [1, 3], [2, 3]], 
		[[1, 2], [2, 3], [1, 3]], 
		[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], 
		[[1, 2], [1, 3], [1, 4], [3, 4], [2, 4]], 
		[[1, 2], [1, 3], [1, 4], [1,5], [2, 3], [2, 4], [2, 5]]
	]

	for i in range(len(edges)):
		print(i+1, ".\tEdges: ", edges[i], sep = "")
		print("\tThe redundant connection in the graph is: ", redundant_connection(edges[i]), sep = "")
		print("-" * 100)

if __name__ == '__main__':
	main()