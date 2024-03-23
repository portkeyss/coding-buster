class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.validIntervals = None #valid intervals entry are sorted in order and each one represents (cumulative count, intervalStart)
        self.m = n
        if len(blacklist)==0:
            self.validIntervals = [[0,0]]
            return
        blacklist.sort()
        blockIntervals = [[blacklist[0], blacklist[0]+1]]
        prev = blacklist[0]
        for num in blacklist[1:]:
            if num==prev+1:
                blockIntervals[-1][1] = num+1
            else:   
                blockIntervals.append([num, num+1])
            prev = num
        points = []
        if blockIntervals[0][0]!=0: points.append(0)
        for a, b in blockIntervals:
            if a!=0:
                points.append(a)
            if b!=n:
                points.append(b)
        if blockIntervals[-1][1]!=n: points.append(n)
        self.validIntervals = []
        count = 0
        for i in range(0,len(points),2):
            self.validIntervals.append([count,points[i]])
            count += points[i+1]-points[i]
        self.m = count
            
    def pick(self) -> int:
        i = randrange(0,self.m)
        j = bisect.bisect_right(self.validIntervals, [i, inf])-1
        return self.validIntervals[j][1]+(i-self.validIntervals[j][0])
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()