from sortedcontainers import SortedList
class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.idxList = SortedList()
        self.A = SortedList(key=lambda x:(-(x[1]//2),x[0])) #self.A is a list of intervals (start, length)

    def seat(self) -> int:
        if not self.idxList:
            self.idxList.add(0)
            return 0
        i, k = self.idxList[0], self.idxList[-1]
        candidates = [] #candidates is list of the candidates (point,length)
        if i>0: candidates.append((0,i))
        if k<self.n-1: candidates.append((k,self.n-1-k))
        if self.A:
            j, d = self.A[0]
            candidates.append((j, d//2))
        candidates.sort(key=lambda x:(-x[1],x[0])) 
        if candidates[0]==(0,i):
            self.idxList.add(0)
            self.A.add(candidates[0])
            return 0
        elif candidates[0]==(k,self.n-1-k):
            self.idxList.add(self.n-1)
            self.A.add(candidates[0])
            return self.n-1
        else:
            j,d = self.A.pop(0)
            self.idxList.add(j+d//2)
            self.A.add(candidates[0])
            self.A.add((j+d//2,(1+d)//2))
            return j+d//2
                
    def leave(self, p: int) -> None:
        j = self.idxList.bisect_left(p)
        if j<len(self.idxList)-1:
            self.A.remove((p,self.idxList[j+1]-p))
        if j>0:
            self.A.remove((self.idxList[j-1],p-self.idxList[j-1]))
        if j>0 and j<len(self.idxList)-1:
            self.A.add((self.idxList[j-1],self.idxList[j+1]-self.idxList[j-1]))
        self.idxList.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)