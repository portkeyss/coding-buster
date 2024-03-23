class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        h = [[] for _ in range(5)]
        h[0].append(0)
        for i in [8,4,2,1]:
            hCopy = [p.copy() for p in h]
            for count,l in enumerate(hCopy):
                for a in l:
                    if a+i < 12:
                        h[count+1].append(a+i)
        
        m = [[] for _ in range(7)]
        m[0].append(0)
        for i in [32,16,8,4,2,1]:
            mCopy = [p.copy() for p in m]
            for count,l in enumerate(mCopy):
                for a in l:
                    if a+i < 60:
                        m[count+1].append(a+i)
        
        res = []
        for x in range(max(0,turnedOn-6), min(4,turnedOn)+1):
            for p in h[x]:
                for q in m[turnedOn-x]:
                    res.append(str(p)+":"+(str(q) if len(str(q))==2 else "0"+str(q)))
        return res