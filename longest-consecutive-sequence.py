# Helper class for making connected components 
class UnionFind:
    # Constructor
    def __init__(self, nums):
        self.parent = {num: num for num in nums}
        self.size = {num: 1 for num in nums}
        self.max_length = 1

    # Function to find the root of a sequence to which num1 belongs
    def find(self, num):
        if self.parent[num] != num:
            self.parent[num] = self.find(self.parent[num])
        return self.parent[num]

    # Function to merge the two sequences and updating lengths
    def union(self, num1, num2):
        x_root = self.find(num1)
        y_root = self.find(num2)
        if x_root != y_root:
            if self.size[x_root] < self.size[y_root]:
                x_root, y_root = y_root, x_root
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
            self.max_length = max(self.max_length, self.size[x_root])

from union_find import UnionFind

def longest_consecutive_sequence(nums):
    if not nums:
        return 0
    uf = UnionFind(nums)
    for num in nums:
        if num + 1 in nums:
            uf.union(num, num + 1)
    
    return uf.max_length

# SOLUTION
from union_find import *

def longest_consecutive_sequence(nums):
    if len(nums) == 0:
        return 0
    # data structure for implementing union find
    ds = UnionFind(nums)

    for num in nums:
        # check if the next consecutive number 
        # is in the input array
        if num + 1 in ds.parent:
            ds.union(num, num + 1)

    return ds.max_length

# driver code
def main():
    input_nums = [
        [150, 14, 200, 1, 3, 2],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 3, 5, 7],
        [7, 6, 5, 4, 3, 2, 1],
        [7, 6, 5, 1],
    ]

    for i in range(0, len(input_nums)):
        print(i+1, ".\tnums = ", input_nums[i], sep="")
        print("\tThe length of the longest consecutive sequence is:", longest_consecutive_sequence(input_nums[i]))
        print("-"*100)

if __name__ == '__main__':
    main()