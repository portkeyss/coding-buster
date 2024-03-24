class SnapshotArray:

    def __init__(self, length: int):
        self.l = [[[-1,0]] for _ in range(length)] # -1 is the snap_id, 0 is the value
        self.sid = -1

    def set(self, index: int, val: int) -> None:
        self.l[index].append([self.sid+1, val])

    def snap(self) -> int:
        self.sid += 1
        return self.sid

    def get(self, index: int, snap_id: int) -> int:
        sid = bisect.bisect(self.l[index], [snap_id+1]) - 1
        return self.l[index][sid][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)