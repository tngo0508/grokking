class UnionFind:
    # Constructor
    def __init__(self):
        self.parents = {}
        self.ranks = {}
        
    # Function to find which group a particular element belongs.
    def find(self, coordinate):
        if coordinate != self.parents[coordinate]:
            self.parents[coordinate] = self.find(self.parents[coordinate])
        return self.parents[coordinate]

    # Function to join two coordinates into a single one.
    def union(self, x, y):
        # Set the parent of each coordinate to itself 
        # if not already present in the dictionary

        self.parents.setdefault(x, x)
        self.parents.setdefault(y, y)

        # Set the ranks of each coordinate to 0 
        # if not already present in the dictionary
        self.ranks.setdefault(x, 0)
        self.ranks.setdefault(y, 0)

        # Compare the ranks of the two coordinates 
        # to decide which should be the parent

        if self.ranks[x] > self.ranks[y]:
            self.parents[self.find(y)] = self.find(x)
        elif self.ranks[y] > self.ranks[x]:
            self.parents[self.find(x)] = self.find(y)
        
         # If the rankss are equal, choose one coordinate 
         # as the parent and increment its ranks
        else:
            self.parents[self.find(x)] = self.find(y)
            self.ranks[y] += 1

# solution
import collections
from collections import defaultdict
from union_find import *


def remove_stones(stones):

    offset = 100000
    stone = UnionFind()

    for x, y in stones:
        stone.union(x, (y + offset))  
    
    groups = set()
    for i in stone.parents:
        groups.add(stone.find(i))

    return len(stones) - len(groups)

# driver code
def main():
    stones = [[[0, 0], [0, 1], [1, 2], [2, 2], [3, 3]],
        [[0, 0], [2, 2], [3, 3]],
        [[0, 1], [2, 1], [3, 0]],
        [[1, 0], [2, 1], [2, 3], [3, 1], [3, 3]],
        [[1, 2], [2, 0], [2, 2], [3, 3]]]

    for i in range(len(stones)):
        print(str(i+1)+".\tMaximum stones which can be removed from "+str(stones[i]) + " are: ", remove_stones(stones[i]))
        print("-" * 100)
  
if __name__ == '__main__':
    main()
