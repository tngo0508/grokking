class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hash_map = {}

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        self.hash_map[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        # print(f"{'remove':*^20}")
        # print(val, self.arr, self.hash_map)
        if val not in self.hash_map:
            return False
        
        last_elem, idx = self.arr[-1], self.hash_map[val]
        self.arr[idx], self.hash_map[last_elem] = last_elem, idx

        del self.hash_map[val]
        self.arr.pop()
        # print(val, self.arr)
        return True

    def getRandom(self) -> int:
        # print(f"{'getRandom':*^20}")
        # print(self.arr)
        # print(self.hash_map)
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()