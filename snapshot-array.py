class SnapshotArray:
    # Constructor
    def __init__(self, length):
        self.arr = [0] * length
        self.snap_shot = {}
        self.snap_id = -1

    # Function set_value sets the value at a given index idx to val. 
    def set_value(self, idx, val):
        self.arr[idx] = val
    
    # This function takes no parameters and returns the snapid.
    # snapid is the number of times that the snapshot() function was called minus 1. 
    def snapshot(self):
        self.snap_id += 1
        self.snap_shot[self.snap_id] = [x for x in self.arr]
        return self.snap_id
    
    # Function get_value returns the value at the index idx with the given snapid.
    def get_value(self, idx, snapid):
        if snapid in self.snap_shot:
            return self.snap_shot[snapid][idx]
        return self.arr[idx % len(self.arr)]

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_shot = {i : {} for i in range(length)}
        self.snap_shot_id = 0

    def set(self, index: int, val: int) -> None:
        self.snap_shot[self.snap_shot_id][index] = val

    def snap(self) -> int:
        clone = copy.deepcopy(self.snap_shot[self.snap_shot_id])
        self.snap_shot_id += 1
        self.snap_shot[self.snap_shot_id] = clone
        return self.snap_shot_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.snap_shot:
            if index in self.snap_shot[snap_id]:
                return self.snap_shot[snap_id][index]
        return 0
        
# SOLUTION
class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.history_records = [[[0, 0]] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        self.history_records[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect_right(self.history_records[index], [snap_id, 10 ** 9])
        return self.history_records[index][snap_index - 1][1]