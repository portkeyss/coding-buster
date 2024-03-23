class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        rows = set()
        cols = set()
        for x1,y1,x2,y2 in rectangles:
            rows.add(x1)
            cols.add(y1)
            rows.add(x2)
            cols.add(y2)
        rows = sorted(list(rows))
        cols = sorted(list(cols))
        res = 0
        m, n = len(rows), len(cols)
        for i in range(m-1):
            for j in range(n-1):
                for x1,y1,x2,y2 in rectangles:
                    if x1<=rows[i]<x2 and y1<=cols[j]<y2:
                        res += (rows[i+1]-rows[i])*(cols[j+1]-cols[j])
                        break
        return res%(10**9+7)