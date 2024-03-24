class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        
        commonNums = set([tops[0], bottoms[0]]) #at most 2 numbers are possible candidate numbers
        for i in range(1,n):
            commonNums &= set([tops[i],bottoms[i]])
            if len(commonNums)==0: return -1
        
        res = inf
        for num in commonNums:
            sameTop = 0
            sameBottom = 0
            for i in range(n):
                if tops[i]!=num: sameTop += 1
                if bottoms[i]!=num: sameBottom += 1
            res = min(res, sameTop, sameBottom)
        return res