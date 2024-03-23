class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        def buildTable(t):
            n = len(t)
            T = [-1]
            pos = 1
            cnd = 0
            for pos in range(1,n):
                if t[pos]==t[cnd]:
                    T.append(T[cnd])
                else:
                    T.append(cnd)
                    while cnd>=0 and t[pos] != t[cnd]:
                        cnd = T[cnd]
                cnd += 1
            T.append(cnd)
            return T
        
        kmpTable = buildTable(b)
        l1, l2 = len(a), len(b)
        j = k = 0
        while j<l1+l2:
            if a[j%l1]==b[k]:
                j += 1
                k += 1
                if k==l2:
                    return (j+l1-1)//l1
            else:
                k = kmpTable[k]
                if k<0:
                    j += 1
                    k += 1
        return -1           