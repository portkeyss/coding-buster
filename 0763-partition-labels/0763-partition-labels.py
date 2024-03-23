class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        count = defaultdict(int)
        for c in S:
            count[c] += 1
        
        res = []
        subCount = defaultdict(int)
        i = -1
        for j,c in enumerate(S):
            subCount[c] += 1
            
            if subCount[c] < count[c]:
                continue
            
            flag = True #All chars in this substring contains all counts of such chars in S
            for c in subCount:
                if subCount[c] != count[c]:
                    flag = False
                    break
            if flag == True:
                res.append(j - i)
                subCount.clear()
                i = j
        return res