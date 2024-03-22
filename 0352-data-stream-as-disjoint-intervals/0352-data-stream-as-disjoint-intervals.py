from sortedcontainers import SortedList
class SummaryRanges:

    def __init__(self):
        self.lst = SortedList()

    def addNum(self, val: int) -> None:
        i = self.lst.bisect_right(val)-1
        if i%2==0: return #already inside an interval 
        self.lst.add(val)
        self.lst.add(val+1)
        j = self.lst.bisect_right(val)-1
        if j-1>=0 and self.lst[j-1]==val:
            del self.lst[j-1:j+1]
        j = self.lst.bisect_right(val+1)-1
        if j-1>=0 and self.lst[j-1]==val+1:
            del self.lst[j-1:j+1]

    def getIntervals(self) -> List[List[int]]:
        even = True
        ans = []
        for a in self.lst:
            if even:
                ans.append([a])
                even = False
            else:
                ans[-1].append(a-1)
                even = True
        return ans


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()